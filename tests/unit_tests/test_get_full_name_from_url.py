import pytest

from racoon.main import get_full_name_from_url

test_cases = [
    ("https://gitlab.com/group/sub/project", "group/sub/project"),
    ("http://git-tea.org/user/project", "user/project"),
    ("https://github.com/user/project", "user/project"),
]


@pytest.mark.parametrize("url,expected", test_cases)
def test_get_fullname_from_url(url: str, expected: str) -> None:
    assert get_full_name_from_url(url) == expected
