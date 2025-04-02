from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipes, name='recipes_ulr'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail_ulr'),
    path('<int:recipe_id>/toggle_favorite/', views.toggle_favorite, name='toggle_favorite_ulr'),
    path('my_favorites', views.my_favorite_recipes, name='my_favorite_recipes_ulr'),

    path('<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe_ulr'),
    path('<int:recipe_id>/edite/', views.edit_recipe, name='edit_recipe_ulr'),

    path('search/', views.search_results, name='search_results_ulr'),
]
