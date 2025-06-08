from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login', 'date_joined', 'get_survey_completed', 'is_active')
    list_filter = ('is_active', 'is_staff', 'date_joined', 'last_login')
    
    def get_survey_completed(self, obj):
        return obj.userprofile.survey_completed if hasattr(obj, 'userprofile') else False
    get_survey_completed.short_description = 'Survey Completed'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
