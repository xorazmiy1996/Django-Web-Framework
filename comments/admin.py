from django.contrib import admin
from .models import Comments

# Register your models here

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'date_created')



admin.site.register(Comments)
