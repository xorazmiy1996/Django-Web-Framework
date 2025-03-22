from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category
from recipes.models import Recipes


# Register your models here.

class RecipeInline(admin.TabularInline):
    model = Recipes
    extra = 1  # Qo'shimcha bo'sh yozuvlar soni

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','date_created')
    date_created = ('date_added',)
    search_fields = ('name',)
    inlines = [RecipeInline]




admin.site.register(Category, CategoryAdmin)

