from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('index', views.index, name='index'),
    
    # Authentication
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),
    
    # Health and Appointment related
    path('appointment-booking', views.appointment_booking, name='appointment-booking'),
    path('appointment-support', views.appointment_support, name='appointment-support'),
    path('chat-bot', views.chat_bot, name='chat-bot'),
    path('contact', views.contact, name='contact'),
    path('contributor', views.contributor, name='contributor'),
    path('health-tracker-new', views.health_tracker_new, name='health-tracker-new'),
    path('survey', views.survey, name='survey'),
    path('test', views.test, name='test'),
]
