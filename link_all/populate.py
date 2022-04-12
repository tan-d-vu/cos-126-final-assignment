import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "link_all.settings")

import django
django.setup()

from django.contrib.auth.models import User
from manage_users.models import Profile
from manage_links.models import Link, SocialMedia
import random

def populate():
    username_prefix = "sample_user_"
    password = "2wsx3edc"

    for x in range(0, 5):
        username = username_prefix + str(x)
        email = username + "@mail.com"
        new_user = add_user(username, email, password)
        add_links(new_user)
        add_social_media(new_user)


def add_user(username, email, password):
    new_user = User.objects.create_user(username, email, password)
    new_user.save()
    return new_user


def add_links(user):
    for x in range(0, 5):
        title = user.username +"'s Link" + str(x)
        url = "https://www.google.com"
        new_link = Link.objects.create(title=title, url=url, user=user)
        new_link.save()

def add_social_media(user):
    for x in range(0, 5):
        name = "facebook"
        url = "https://www.facebook.com"
        new_social_media = SocialMedia.objects.create(name=name, url=url, user=user)
        new_social_media.save()

if __name__ == '__main__':
    print("Populating the database...")
    populate()
    print("Finished.")