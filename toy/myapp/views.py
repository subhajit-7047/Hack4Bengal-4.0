from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password!')
            
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return render(request, 'signup.html')
            
        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user)
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
        
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('login')

def appointment_booking(request):
    return render(request, 'appointment-booking.html')

def appointment_support(request):
    return render(request, 'appointment-support.html')

def chat_bot(request):
    return render(request, 'chat_bot.html')

def contact(request):
    return render(request, 'contact.html')

def contributor(request):
    return render(request, 'contributor.html')

def health_tracker_new(request):
    return render(request, 'health-tracker-new.html')

def survey(request):
    return render(request, 'survey.html')

def test(request):
    return render(request, 'test.html')
