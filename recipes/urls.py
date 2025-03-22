from django.urls import path
from . import views
app_name = 'recipes'

urlpatterns = [
    path('', views.recipes, name='index'),
    path('recipes/<int:recipe_id>', views.recipe, name='recipe_url'),
]