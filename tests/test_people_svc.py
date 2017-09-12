
import pytest
from api import PeopleSvc


@pytest.fixture
def svc():
    return PeopleSvc()


def test_get_person(svc):
    response = svc.get_person(1)
    assert response.ok
    assert response.status_code == 200
    assert response.json()['name'] == "Luke Skywalker"
