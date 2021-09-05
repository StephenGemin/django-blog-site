from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Used in the function view approach. Defines your own custom forms
# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#
#
# class ProfileUpdateForm(forms.ModelForm):
#
#     class Meta:
#         model = Profile
#         fields = ['image']
