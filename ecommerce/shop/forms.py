from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phonenumber = forms.CharField(max_length=11)
    telephone = forms.CharField(max_length=11)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ContactUsForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
