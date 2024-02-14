from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Option

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class VotingForm(forms.Form):
    option = forms.ModelChoiceField(queryset=Option.objects.all(), empty_label=None, widget=forms.RadioSelect)
    

