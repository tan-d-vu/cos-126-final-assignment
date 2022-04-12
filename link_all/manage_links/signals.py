from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Link
from manage_users.models import Profile


@receiver(post_save, sender=Profile)
def create_link(sender, instance, created, **kwargs):
    if created:
        url = "http://localhost:8000/profile/" + instance.user.username
        Link.objects.create(user=instance.user, title="My LinkAll Page", url=url)
