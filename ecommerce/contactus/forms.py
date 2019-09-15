from django import forms


class ContactUsForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)