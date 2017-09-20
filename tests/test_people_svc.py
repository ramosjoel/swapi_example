
import pytest
from api import PeopleSvc


@pytest.fixture
def svc():
    return PeopleSvc()


def test_get_person(svc):
    person = svc.get_person(1)
    response = svc.history[-1]
    assert response.ok
    assert response.status_code == 200
    assert response.json()['name'] == "Luke Skywalker"
    assert response.name == 'Luke Skywalker'
    assert person.birth_year == '19BBY'


