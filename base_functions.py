import random

import requests as requests

from config import config
from constants import BASE_API_URL


def signup_user(username, password, email: str):
    random_string_number = ""

    while True:
        data = {
            "username": username + str(random_string_number),
            "password": password,
            "email": _insert_string_before_at(email, random_string_number),
        }
        response = requests.post(BASE_API_URL + "signup/", data=data)
        if response.status_code == 201:
            break
        random_string_number = str(
            random.randint(config["number_of_users"], config["number_of_users"] * 100)
        )
    return response.json()


def _insert_string_before_at(email, string_to_insert):
    username, domain = email.split("@")
    new_email = f"{username}{string_to_insert}@{domain}"
    return new_email


def create_post(token, title, content):
    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": title, "content": content}
    response = requests.post(BASE_API_URL + "posts/create/", headers=headers, data=data)
    return response.json()


def like_post(token, post_id):
    headers = {"Authorization": f"Bearer {token}"}
    requests.post(BASE_API_URL + f"posts/{post_id}/like/", headers=headers)
