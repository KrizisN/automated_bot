import random

from base_functions import signup_user, create_post, like_post
from config import config


def run():
    users = _create_users()
    posts = _create_posts(users)
    _like_posts(posts, users)


def _create_users():
    users = []
    for i in range(config.get("number_of_users", 10)):
        user = signup_user(f"user{i}", "password123", f"user{i}@gmail.com")
        users.append(user)
    return users


def _create_posts(users):
    posts = []
    for user in users:
        token = user["access"]
        num_posts = random.randint(1, config.get("max_posts_per_user", 10))
        for _ in range(num_posts):
            post = create_post(token, "Test title", "Test content")
            posts.append(post)
    return posts


def _like_posts(posts, users):
    for user in users:
        token = user["access"]
        num_likes = random.randint(1, config.get("max_likes_per_user", 10))
        for _ in range(num_likes):
            post_id = random.choice(posts)["id"]
            like_post(token, post_id)


if __name__ == "__main__":
    run()
