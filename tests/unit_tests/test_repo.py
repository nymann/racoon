import pytest

from racoon.repo import Repo

test_cases = [
    ("https://gitlab.com/group/sub/project", Repo(group="sub", name="project")),
    ("http://git-tea.org/user/project", Repo(group="user", name="project")),
    ("https://github.com/user/project", Repo(group="user", name="project")),
]


@pytest.mark.parametrize("url,expected", test_cases)
def test_get_fullname_from_url(url: str, expected: Repo) -> None:
    actual = Repo.from_url(url)
    assert actual == expected
