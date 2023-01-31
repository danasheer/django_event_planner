from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }

