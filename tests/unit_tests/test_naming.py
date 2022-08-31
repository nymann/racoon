import pytest

from racoon.template_generation import package_name
from racoon.template_generation import project_name
from racoon.template_generation import sanitize_repo_name

test_cases = [
    "ProjectName",
    "project_name",
    "project name",
    "Project Name",
    "ProjectName ",
    "projectName",
    "-projectName",
    "   projectName",
]


@pytest.mark.parametrize("unsafe_repo_name", test_cases)
def test_repo_name(unsafe_repo_name: str) -> None:
    actual = sanitize_repo_name(unsafe_repo_name=unsafe_repo_name)
    assert "project-name" == actual


@pytest.mark.parametrize("unsafe_repo_name", test_cases)
def test_project_name(unsafe_repo_name: str) -> None:
    sanitized = sanitize_repo_name(unsafe_repo_name=unsafe_repo_name)
    actual = project_name(safe_repo_name=sanitized)
    assert "Project Name" == actual


@pytest.mark.parametrize("unsafe_repo_name", test_cases)
def test_package_name(unsafe_repo_name: str) -> None:
    sanitized = sanitize_repo_name(unsafe_repo_name=unsafe_repo_name)
    actual = package_name(safe_repo_name=sanitized)
    assert "project_name" == actual
