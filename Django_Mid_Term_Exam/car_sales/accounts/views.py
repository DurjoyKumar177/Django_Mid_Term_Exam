from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import RegisterForm, ChangeUserData
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from orders.models import Order

def profile_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})

class SignupView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login') 
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
                return redirect('profile')  # Redirect to profile page
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, 'login.html', {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully.')
        return redirect('login')


class Profile_editView(LoginRequiredMixin, View):
    def get(self, request):
        form = ChangeUserData(instance=request.user)
        return render(request, 'profile_edit.html', {'form': form})

    def post(self, request):
        form = ChangeUserData(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully.')
            return redirect('profile_edit')
        return render(request, 'profile_edit.html', {'form': form})


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
