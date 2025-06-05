from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import * 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

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
