from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('index', views.index),
    
    # Authentication and User Management
    path('login', views.login),
    path('signup', views.signup),
    
    # Health and Appointment related
    path('appointment-booking', views.appointment_booking),
    path('appointment-support', views.appointment_support),
    path('chat-bot', views.chat_bot),
    path('contact', views.contact),
    path('contributor', views.contributor),
    path('health-tracker-new', views.health_tracker_new),
    path('survey', views.survey),
    path('test', views.test),
]
