from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Album
from .forms import AlbumForm

@login_required
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form})

@login_required
def edit_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form})

@login_required
def delete_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    album.delete()
    return redirect('homepage')
