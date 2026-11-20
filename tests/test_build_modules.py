"""The build's modules import without network access or a built site."""


def test_build_modules_import():
    import create_static_html_files  # noqa: F401
    import fetch_napari_data  # noqa: F401
