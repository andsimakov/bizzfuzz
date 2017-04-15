from random import randint
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Required. Letters, digits and @/./+/-/_ only.'}))

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Required'}))

    password2 = forms.CharField(
        label='Conform Password',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter the same password as before, for verification'}))

    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Required. user@example.com'}))

    birthday = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Required. Enter as YYYY-MM-DD'}))

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=commit)
        user_profile = Profile.objects.create(
            user=user,
            birthday=self.cleaned_data['birthday'],
            random=randint(1, 100),
        )
        return user_profile
