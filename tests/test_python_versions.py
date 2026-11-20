"""Python versions shown on plugin pages and offered to the search filter (hub-lite#143)."""

from types import SimpleNamespace

from create_static_html_files import (
    classifier_python_versions,
    generate_python_versions_html,
)

CLASSIFIERS = [
    "Framework :: napari",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]


def page(classifiers, requires_python):
    plugin = SimpleNamespace(
        package_metadata_classifiers=classifiers,
        package_metadata_requires_python=requires_python,
    )
    return generate_python_versions_html(plugin)


def test_classifier_versions_sort_by_minor():
    assert classifier_python_versions(
        [
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.8",
        ]
    ) == ["3.8", "3.9", "3.10"]


def test_classifiers_are_shown_and_filtered_even_when_requires_python_differs():
    html, text, filters = page(CLASSIFIERS, ">=3.8,<3.10")
    assert text == "3.10, 3.11, 3.12"
    assert "?python=3.11" in html
    assert "3.8" not in html
    assert filters.count('data-pagefind-filter="python_versions"') == 3


def test_without_classifiers_requires_python_is_shown_as_written():
    html, text, filters = page(["Framework :: napari"], ">=3.9,<3.13")
    assert "&gt;=3.9,&lt;3.13" in html
    assert text == "&gt;=3.9,&lt;3.13"
    assert filters == ""


def test_nothing_declared_is_not_specified():
    html, text, filters = page([], "")
    assert "Not specified" in html
    assert text == "Not specified"
    assert filters == ""
