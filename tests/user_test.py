import pytest
import asyncio
from fastapi.testclient import TestClient
from main import app
from . import create_valid_user
from http import HTTPStatus

@pytest.mark.asyncio
async def test_register_user():
    client = TestClient(app)
    new_user: dict = create_valid_user()
    response  = client.post('/user/register', json=new_user)
    assert response.status_code == HTTPStatus.OK
    assert response.json()['username'] == new_user['username']