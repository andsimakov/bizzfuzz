from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from random import randint
from .models import User, Profile


# class UserForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['email', 'username', 'password', 'first_name', 'last_name', 'random']
#         # help_texts = {
#         #     'email': 'Required. account@example.com',
#         #     'username': 'Required. Letters, digits and @/./+/-/_ only',
#         #     'password': 'Required',
#         #     'birthday': 'Required. YYYY-MM-DD',
#         # }


class ProfileForm(UserCreationForm):
    birthday = forms.DateField(
        help_text='Required.',
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=commit)
        user_profile = Profile.objects.create(
            user=user,
            birthday=self.cleaned_data['birthday'],
            random_number=randint(1, 100),
        )

        return user_profile
