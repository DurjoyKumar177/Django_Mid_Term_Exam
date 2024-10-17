from django.urls import path
from . import views

urlpatterns = [
    path('add-album/', views.create_album, name='add_album'),
    path('edit-album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete-album/<int:album_id>/', views.delete_album, name='delete_album'),
]
