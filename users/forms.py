from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# Creating a custom form class by inheriting from 'UserCreationForm'


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  # add the new custom field

    class Meta:  # meta class tells what do with parent form class
        model = User  # save data of this class to model 'User'

        fields = ['username', 'email', 'password1', 'password2']
        # form will have these fields in this order


class UserUpdateForm(forms.ModelForm):
    # ModelForm allow to create form for a specific database model
    email = forms.EmailField()

    class Meta:
        model = User  # save data of this class to model 'User'

        fields = ['username', 'email']
        # form will have these fields in this order


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile  # save data of this class to model 'User'

        fields = ['image']
