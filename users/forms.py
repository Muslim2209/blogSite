from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']

    def clean_email(self):
        emails = User.objects.values_list('email', flat=True)
        email = self.cleaned_data['email']
        if email in emails:
            raise forms.ValidationError("This email already registered.")
        return email
