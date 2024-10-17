from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Musician
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import MusicianForm, RegisterForm, ChangeUserData
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

# Create your views here.

class HomeView(View):
    def get(self, request):
        musicians = Musician.objects.all()
        return render(request, 'home.html', {'musicians': musicians})

@method_decorator(login_required, name='dispatch')
class CreateMusicianView(View):
    def get(self, request):
        form = MusicianForm()
        return render(request, 'musician_form.html', {'form': form})

    def post(self, request):
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Musician created successfully.')
            return redirect('homepage')
        return render(request, 'musician_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class EditMusicianView(View):
    def get(self, request, musician_id):
        musician = get_object_or_404(Musician, id=musician_id)
        form = MusicianForm(instance=musician)
        return render(request, 'musician_form.html', {'form': form})

    def post(self, request, musician_id):
        musician = get_object_or_404(Musician, id=musician_id)
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            messages.success(request, 'Musician updated successfully.')
            return redirect('homepage')
        return render(request, 'musician_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(View):
    def post(self, request, musician_id):
        musician = get_object_or_404(Musician, id=musician_id)
        musician.delete()
        messages.success(request, 'Musician deleted successfully.')
        return redirect('homepage')


class SignupView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Redirect to login after successful signup
        return render(request, 'signup.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('profile')  
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, 'login.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully.')
        return redirect('login')

@method_decorator(login_required, name='dispatch')
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = ChangeUserData(instance=request.user)
        return render(request, 'profile.html', {'form': form})

    def post(self, request):
        form = ChangeUserData(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully.')
            return redirect('profile')
        return render(request, 'profile.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class PassChangeView(LoginRequiredMixin, View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully.')
            return redirect('profile')
        return render(request, 'passchange.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class PassChange2View(LoginRequiredMixin, View):
    def get(self, request):
        form = SetPasswordForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})

    def post(self, request):
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password set successfully.')
            return redirect('profile')
        return render(request, 'passchange.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ChangeUserDataView(LoginRequiredMixin, View):
    def get(self, request):
        form = ChangeUserData(instance=request.user)
        return render(request, 'profile.html', {'form': form})

    def post(self, request):
        form = ChangeUserData(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User data updated successfully.')
            return redirect('profile')
        return render(request, 'profile.html', {'form': form})
