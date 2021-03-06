from logging import PlaceHolder
from django.db import models
from django.contrib.auth.models import User

# Link model
class Link(models.Model):
    url = models.URLField(blank=False)
    title = models.CharField(blank=False, max_length=300)

    # Many to One with user model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Social Media Buttons
class SocialMedia(models.Model):
    """
    Bug: Missing blank=False field, user can create blank links
    => Add it back in
    Student have to identify bug from assignment specs
    """
    SOCIAL_MEDIA_CHOICES = (
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("youtube", "YouTube"),
        ("twitter", "Twitter"),
        ("spotify", "Spotify"),
        ("reddit", "Reddit")
    )
    url = models.URLField(blank=False)
    name = models.CharField(blank=False, max_length=300, choices=SOCIAL_MEDIA_CHOICES)
    # Many to One with user model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
