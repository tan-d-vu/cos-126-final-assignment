from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Link model
class Link(models.Model):
    url = models.URLField(blank = False)
    title = models.CharField(blank = False, max_length = 300)
    
    # Many to One with user model
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

# Social Media Buttons
class SocialMedia(models.Model):
    url = models.URLField(blank=False)
    name = models.CharField(blank=False, max_length = 300)
    # Many to One with user model
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

