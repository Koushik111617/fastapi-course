from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db, Base
from alembic import command
from app.oauth2 import create_access_token
from app import models

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
testingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#scope can be function, module, session
# @pytest.fixture(scope='module')
@pytest.fixture()
def session():
    print('My session fixture ran')
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = testingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def overrid_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = overrid_get_db
    yield TestClient(app)

@pytest.fixture
def test_user(client):
    user_data = {"email": "koushik@gmail.com", "password": 'password123'}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    print("test_user_id",  test_user['id'])
    return create_access_token({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(test_user, session):
    posts_data = [{
        "title": "first title",
        "content": "first content",
        "owner_id": test_user['id']
    }, {
        "title": "second title",
        "content": "second content",
        "owner_id": test_user['id']
    }, {
        "title": "third title",
        "content": "third content",
        "owner_id": test_user['id']
    }]

    def create_user_model(post):
        return models.Post(**post)
    post_map = map(create_user_model, posts_data)
    posts = list(post_map)
    session.add_all(posts)
    # session.add_all([models.Post(title="first title", content="first content", owner_id=test_user['id']),
    #                 models.Post(title="second title", content="second content", owner_id = test_user['id']),
    #                 models.Post(title="third title", content="third content", owner_id = test_user['id']),
    # ])
    session.commit()
    posts = session.query(models.Post).all()
    return posts