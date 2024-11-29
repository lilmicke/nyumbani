from django.db import models
from django.conf import settings

# Define the Property model
class Property(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    property_image = models.ImageField(upload_to='property_images/', blank=True, null=True)  # Optional image field

    def __str__(self):
        return f"Property {self.id} at {self.location}"

# Define the UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)  # Optional bio
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Optional profile picture

    def __str__(self):
        return f"Profile of {self.user.username}"

    # Optionally, you could add a method to return the full URL for the profile picture.
    def get_profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return "/static/default-profile-picture.png"  # Replace with a default image if none is uploaded

# Define the CustomUser model
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Additional fields or methods for the custom user model
    pass
