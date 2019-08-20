from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()  

class LoginForm(forms.Form):
    username = forms.CharField(min_length=4)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=4)
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label= "Confirm password", widget=forms.PasswordInput())

    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already taken")
        return username

    def clean_email(self):
        email=self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email already used")
        return email

    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get("password")
        password2=self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Passwords must match")
        return data