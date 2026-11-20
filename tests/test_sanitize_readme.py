"""A README can't run code on its hub page, and keeps its formatting."""

import pytest

from create_static_html_files import md, sanitize_readme_html


def render_readme(markdown: str) -> str:
    """Render a README the way a plugin page does."""
    return sanitize_readme_html(md.render(markdown))


@pytest.mark.parametrize(
    ("markdown", "forbidden"),
    [
        ("<script>alert(1)</script>\n", "<script"),
        ('<img src="x.png" onerror="alert(1)">\n', "onerror"),
        ('<a href="https://example.org" onclick="alert(1)">x</a>\n', "onclick"),
        ('<iframe src="https://example.org"></iframe>\n', "<iframe"),
        ('<a href="javascript:alert(1)">x</a>\n', "javascript:"),
        ("[x](javascript:alert(1))\n", 'href="javascript:'),
        ("<svg><script>alert(1)</script></svg>\n", "<script"),
        ('<p style="position:fixed;inset:0">cover the page</p>\n', "style="),
        (
            '<form action="https://example.org"><input name="password"></form>\n',
            "<form",
        ),
        ('<object data="x.swf"></object>\n', "<object"),
        ('<meta http-equiv="refresh" content="0;url=https://example.org">\n', "<meta"),
    ],
)
def test_code_and_tricks_are_removed(markdown, forbidden):
    assert forbidden not in render_readme(markdown)


def test_highlighted_code_keeps_its_classes():
    html = render_readme("```python\nimport napari\n```\n")
    assert '<code class="language-python">' in html
    assert '<div class="highlight">' in html
    assert '<span class="kn">import</span>' in html


@pytest.mark.parametrize(
    ("markdown", "kept"),
    [
        (
            '<p align="center"><img src="https://x.org/logo.png" width="200" alt="logo"></p>\n',
            ['<p align="center">', 'width="200"', 'alt="logo"'],
        ),
        (
            '<picture><source media="(prefers-color-scheme: dark)" srcset="https://x.org/d.png">'
            '<img src="https://x.org/l.png" alt="logo"></picture>\n',
            [
                "<picture>",
                'media="(prefers-color-scheme: dark)"',
                'srcset="https://x.org/d.png"',
            ],
        ),
        (
            "<details><summary>More</summary>\n\nHidden text\n\n</details>\n",
            ["<details>", "<summary>More</summary>"],
        ),
        ("| a | b |\n|---|---|\n| 1 | 2 |\n", ["<table>", "<td>1</td>"]),
        ("[docs](https://example.org)\n", ['href="https://example.org"']),
    ],
)
def test_readme_formatting_is_kept(markdown, kept):
    html = render_readme(markdown)
    for fragment in kept:
        assert fragment in html


def test_table_alignment_is_kept():
    html = render_readme("| a |\n|--:|\n| 1 |\n")
    assert '<td style="text-align:right">1</td>' in html


def test_only_harmless_style_properties_survive():
    html = render_readme(
        '<img src="https://x.org/a.png" style="max-width:100%;position:fixed;'
        'background:url(https://example.org/track)">\n',
    )
    assert 'style="max-width:100%"' in html
    assert "position" not in html
    assert "url(" not in html


def test_videos_play_but_cannot_run_code():
    html = render_readme(
        '<video src="https://github.com/user-attachments/assets/x.mp4" controls '
        'onplay="alert(1)"></video>\n',
    )
    assert '<video src="https://github.com/user-attachments/assets/x.mp4"' in html
    assert "onplay" not in html


def test_links_open_without_giving_the_page_away():
    html = render_readme("[docs](https://example.org)\n")
    assert 'rel="noopener noreferrer"' in html
