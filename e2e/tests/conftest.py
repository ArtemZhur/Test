import pytest

from e2e.services.courses import Courses


@pytest.fixture(scope="function")
def courses_handler():
    return Courses()
