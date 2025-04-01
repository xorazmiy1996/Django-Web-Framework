from django.urls import path
from . import views
app_name = 'recipes'

urlpatterns = [
    path('', views.recipes, name='recipes_ulr'),
    path('/<int:recipe_id>', views.recipe_detail, name='recipe_detail_ulr'),
    path('/<int:recipe_id>/toggle_favorite', views.toggle_favorite, name='toggle_favorite_ulr'),
    path('search/', views.search_results, name='search_results_ulr'),
]