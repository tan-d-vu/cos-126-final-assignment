from django.db import models
from django.contrib.auth.models import User

# User Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    display_name = models.CharField(max_length = 200, blank = True)
    bio = models.TextField()
    """
    Bug: Missing uploead_to field => Add it back in
    """
    profile_photo = models.ImageField(blank = True, upload_to = "pfp")
    background_photo = models.ImageField(blank = True, upload_to = "bgp")

    def __str__(self):
        return self.user.username