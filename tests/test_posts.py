from typing import List
from app import schemas
from pydantic import ValidationError, validate_call
def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    print(res.json())
    # def validate(post):
    #     return schemas.PostOut(**post)
    # posts_map = map(validate, res.json())
    # post_list = list(posts_map)
    # print(post_list)
    # assert post_list[0].Post_id == test_posts[0].id
    assert res.status_code == 200
    assert len(res.json()) == len(test_posts)


def test_unauthorized_user_get_one_posts(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/8888")
    assert res.status_code == 404


def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    print(res.json())
    res_data = res.json()
    transformed_data = {
        "Post": res_data,
        "votes": 0
    }
    post = schemas.PostOut(**transformed_data)
    print(post)
    assert post.Post.title == test_posts[0].title
    assert post.votes == 0
