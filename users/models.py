from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    # user profile have one to one relationship with User model
    # on delete of User object, related profile object will also be deleted,
    # but not the other way around.

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # pictures wll be stored in the profile_pics/ dir.

    def __str__(self):
        return f'{self.user.username} Profile'
