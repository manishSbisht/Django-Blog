from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user profile have one to one relationship with User model
    # on delete of User object, related profile object will also be deleted,
    # but not the other way around.

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # pictures wll be stored in the profile_pics/ dir.

    def __str__(self):
        return f'{self.user.username} Profile'

    """  
    overriding default save method below.
    To preserve its signature, *args & **kwargs must be passed after modification
    """

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # run the defaut save fucntion, then
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
