import pytest
from jsonschema import ValidationError, validate

from e2e.validation.parser import get_template, get_limit_value


def test_basic(courses_handler):
    response = courses_handler.get_courses()
    assert response.status_code == 200

    try:
        validate(instance=response.json(), schema=get_template('ImageSimilarityResponse'))
    except ValidationError:
        pytest.fail("Validation failed")


@pytest.mark.parametrize(
    "limit",
    [
        pytest.param("limit=1"),
        pytest.param("limit=3"),
        pytest.param("limit=5"),
    ])
def test_limit(courses_handler, limit):
    response = courses_handler.get_courses(limit)
    assert response.status_code == 200
    assert len(response.json()) == get_limit_value(limit)


@pytest.mark.parametrize(
    "sort",
    [
        pytest.param("sort=asc"),
        pytest.param("sort=desc"),
    ])
def test_asc_desc(courses_handler, sort):
    response = courses_handler.get_courses(sort)
    assert response.status_code == 200
    if 'asc' in sort:
        assert response.json()[0]['id'] > response.json()[1]['id']
    elif 'desc' in sort:
        assert response.json()[0]['id'] < response.json()[1]['id']

