import sys
import pytest

sys.path.append('.')


@pytest.fixture
def client():
    from app import create_app
    return create_app().test_client()


def test_add(client):
    resp = client.get('/add/a=5.0&b=5.5')

    assert resp.status_code == 200
    assert resp.data == b'10.5'


def test_sub(client):
    resp = client.get('/sub/a=5.0&b=5.5')

    assert resp.status_code == 200
    assert resp.data == b'-0.5'
