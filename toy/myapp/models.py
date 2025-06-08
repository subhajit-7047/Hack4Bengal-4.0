from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    last_survey_date = models.DateTimeField(null=True, blank=True)
    survey_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
