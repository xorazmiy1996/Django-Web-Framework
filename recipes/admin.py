from django.contrib import admin
from .models import Recipes
from comments.models import Comments
# Register your models here.

class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id','name','date_created')

    inlines = [CommentsInline]

admin.site.register(Recipes, RecipeAdmin)