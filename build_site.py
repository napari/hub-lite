from __future__ import annotations

import argparse
import contextlib
import http.server
import os
import shutil
import socketserver
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_BUILD_DIR = ROOT / "_build"
ASSET_DIRS = (
    (ROOT / "templates", "templates"),
    (ROOT / "static" / "images", "static/images"),
    (ROOT / "static" / "css", "static/css"),
    (ROOT / "static" / "js", "static/js"),
)
ASSET_FILES = (
    (ROOT / "index.html", "index.html"),
    (ROOT / "404.html", "404.html"),
)


def in_managed_environment() -> bool:
    return any(
        os.environ.get(name)
        for name in (
            "VIRTUAL_ENV",
            "CONDA_DEFAULT_ENV",
            "CONDA_PREFIX",
            "PIXI_PROJECT_NAME",
            "PIXI_ENVIRONMENT_NAME",
        )
    )


def in_ci() -> bool:
    return os.environ.get("CI") == "true" or os.environ.get("GITHUB_ACTIONS") == "true"


def require_environment() -> None:
    if in_ci():
        print("Running in CI - skipping virtual environment check.")
        return

    if in_managed_environment():
        print("Managed Python environment detected.")
        return

    raise SystemExit("Please activate a virtual environment first (venv, conda, or pixi).")


def copy_tree(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def prepare_build_directory(build_dir: Path) -> None:
    build_dir.mkdir(parents=True, exist_ok=True)

    for source, relative_destination in ASSET_DIRS:
        copy_tree(source, build_dir / relative_destination)

    for source, relative_destination in ASSET_FILES:
        copy_file(source, build_dir / relative_destination)


def run_script(script_name: str, build_dir: Path) -> None:
    require_environment()
    subprocess.run(
        [sys.executable, str(ROOT / script_name), str(build_dir)],
        check=True,
        cwd=ROOT,
    )


def clean(build_dir: Path) -> None:
    shutil.rmtree(build_dir, ignore_errors=True)


def prep(build_dir: Path) -> None:
    prepare_build_directory(build_dir)


def fetch_data(build_dir: Path) -> None:
    prepare_build_directory(build_dir)
    (build_dir / "data").mkdir(parents=True, exist_ok=True)
    run_script("fetch_napari_data.py", build_dir)


def create_html(build_dir: Path) -> None:
    fetch_data(build_dir)
    (build_dir / "plugins").mkdir(parents=True, exist_ok=True)
    run_script("create_static_html_files.py", build_dir)


def build_all(build_dir: Path) -> None:
    create_html(build_dir)


def serve_local(build_dir: Path, host: str, port: int) -> None:
    build_all(build_dir)

    handler = lambda *args, **kwargs: http.server.SimpleHTTPRequestHandler(  # noqa: E731
        *args,
        directory=str(build_dir),
        **kwargs,
    )

    with contextlib.suppress(KeyboardInterrupt):
        with socketserver.TCPServer((host, port), handler) as httpd:
            print(f"Serving HTTP on {host} port {port} (http://{host}:{port}/) ...")
            httpd.serve_forever()


def build_parser() -> argparse.ArgumentParser:
    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument(
        "--build-dir",
        default=str(DEFAULT_BUILD_DIR),
        help="Target build directory. Defaults to ./_build.",
    )

    parser = argparse.ArgumentParser(description="Build and serve the hub-lite site.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("clean", "prep", "fetch-data", "create-html", "all"):
        subparsers.add_parser(command, parents=[shared])

    serve_parser = subparsers.add_parser("serve-local", parents=[shared])
    serve_parser.add_argument("--host", default="127.0.0.1")
    serve_parser.add_argument("--port", type=int, default=8000)

    return parser


def main() -> None:
    args = build_parser().parse_args()
    build_dir = Path(args.build_dir).resolve()

    if args.command == "clean":
        clean(build_dir)
    elif args.command == "prep":
        prep(build_dir)
    elif args.command == "fetch-data":
        fetch_data(build_dir)
    elif args.command == "create-html":
        create_html(build_dir)
    elif args.command == "all":
        build_all(build_dir)
    elif args.command == "serve-local":
        serve_local(build_dir, args.host, args.port)


if __name__ == "__main__":
    main()