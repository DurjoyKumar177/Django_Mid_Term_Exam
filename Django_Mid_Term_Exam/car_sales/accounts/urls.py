from django.urls import path
from .views import profile_view
from .views import (
    SignupView,
    UserLoginView,
    UserLogoutView,
    Profile_editView,
    PassChangeView,
    PassChange2View,
)

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('pass_change/', PassChangeView.as_view(), name='passchange'),
    path('pass_change2/', PassChange2View.as_view(), name='passchange2'),
    path('profile_edit/', Profile_editView.as_view(), name='profile_edit'),
]
