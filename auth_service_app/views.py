from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from datetime import date
from auth_service_app.forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserUpdateForm, CustomPasswordChangeForm, CustomUserCreationRoleForm
from auth_service_app.models import CustomUser



# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('panel')
    return render(request, 'index.html')

def log_in(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        user = CustomUser.objects.filter(email=request.POST.get('username')).first()
        
        if not user:
            messages.error(request, "Credenciales incorrectas. Inténtalo de nuevo")
            return redirect('login')

        if user.is_active == False:
            messages.error(request, "Tu cuenta está inactiva. Contacta al administrador")
            return redirect('login') 

        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('panel')
        else:
            messages.error(request, "Credenciales incorrectas. Inténtalo de nuevo")
            return redirect('login')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('home')

def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('panel')

    return render(request, 'register.html', {'form': form})
