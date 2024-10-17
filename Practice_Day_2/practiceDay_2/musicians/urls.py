from django.urls import path
from .views import (
    HomeView,
    CreateMusicianView,
    EditMusicianView,
    DeleteMusicianView,
    SignupView,
    UserLoginView,
    UserLogoutView,
    ProfileView,
    PassChangeView,
    PassChange2View,
)

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('add-musician/', CreateMusicianView.as_view(), name='add_musician'),
    path('edit-musician/<int:musician_id>/', EditMusicianView.as_view(), name='edit_musician'),
    path('delete-musician/<int:musician_id>/', DeleteMusicianView.as_view(), name='delete_musician'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('pass_change/', PassChangeView.as_view(), name='passchange'),
    path('pass_change2/', PassChange2View.as_view(), name='passchange2'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
