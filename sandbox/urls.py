
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list-url'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail-url'),
]