import pytest
from jose import jwt
from app import schemas
# from .database import client, session
from app.config import settings



# def test_root(client):
#     res = client.get("/")
#     print(res.json().get('message'))
#     assert res.json().get('message') == 'bind mount worked'
#     assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "hello2@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert res.status_code == 201
    assert new_user.email == "hello2@gmail.com"

def test_login_user(client, test_user):
    res = client.post(
        "/login", data={"username": test_user['email'], "password":test_user['password']})
    print(res.json())
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id: str = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'password123', 403),
    ("koushik@gmail.com", 'wrongPassword', 403),
    ('wrongemail@gmail.com', 'wrongPassword', 403)
    # (None, 'password123, 422'),
    # ("koushik@gmail.com", None, 422)    # schema validation fails, so 422
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials...'
