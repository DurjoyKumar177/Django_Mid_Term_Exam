from django import forms
from .models import Musician
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'instrument_type']

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    
    usable_password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    