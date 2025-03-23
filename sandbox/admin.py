from django.contrib import admin

from sandbox.models import Feedback

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Feedback)