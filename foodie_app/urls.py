from django.urls import path
from . import views

app_name = 'foodie_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:category_id>', views.recipes, name='recipes_ulr'),
    path('add-category/', views.add_category, name='add-category-ulr'),
    path('add-recipe/', views.add_recipe, name='add-recipe-ulr'),
    path('add-recipe/category/<int:category_id>/', views.add_recipe, name='add-recipe-with-ulr'),
]