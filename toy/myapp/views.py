from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'index.html')

def login(request):
    # If user wants to login again, log them out first
    if request.user.is_authenticated:
        logout(request)
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            
            # Check if survey needs to be retaken
            profile = UserProfile.objects.get_or_create(user=user)[0]
            if not profile.survey_completed:
                return redirect('survey')
                
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'login.html')

def signup(request):
    # If user wants to signup while logged in, log them out first
    if request.user.is_authenticated:
        logout(request)
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'signup.html')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return render(request, 'signup.html')
            
        # Create user with email as username
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        # Create user profile
        UserProfile.objects.create(user=user)
        
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
        
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def survey(request):
    return render(request, 'survey.html')

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

def test(request):
    return render(request, 'test.html')
