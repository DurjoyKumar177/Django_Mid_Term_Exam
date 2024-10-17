from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'title', 'description', 'price', 'quantity', 'image']
