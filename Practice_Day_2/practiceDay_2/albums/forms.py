from django import forms
from .models import Album


# Album form
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['musician', 'album_name', 'release_date', 'rating']
