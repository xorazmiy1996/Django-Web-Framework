from django.contrib import admin
from django.contrib.auth.models import User

from accounts.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('id','bio', 'date_created',)

admin.site.register(UserProfile, UserProfileAdmin)
