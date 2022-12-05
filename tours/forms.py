from django import forms
import tinymce
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from tinymce.widgets import TinyMCE

from .models import Destination, Post, User


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Destination
        fields = '__all__'


# class PostForm(forms.ModelForm):
#     content = forms.CharField(
#         attrs={'required': False, 'cols': 30, 'rows': 10}
#
#     )
#
#     class Meta:
#         model = Destination
#         fields = '__all__'
#

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already exist')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already exist')
        return username


class CreatePostForm(ModelForm):
    title = forms.CharField()
    caption = forms.CharField(widget=forms.Textarea(attrs={"rows": "5"}))

    class Meta:
        model = Post
        fields = ['image_path', 'caption', 'title']


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'profile_pic']