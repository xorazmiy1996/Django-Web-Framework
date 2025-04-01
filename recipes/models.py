from django.contrib.admin import TabularInline
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from foodie_app.models import Category


# Create your models here.



class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    favorited_by = models.ManyToManyField(User, related_name='favorite_recipes', blank=True)
    image = models.ImageField(upload_to="recipe_images",null=True, blank=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipes:recipe_detail_ulr', kwargs={'recipe_id': self.pk})
