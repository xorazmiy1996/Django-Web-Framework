from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from recipes.models import Recipes


def index(request):
    data = {"name":"Paulo", "age":123}
    return render(request, 'sandbox/index.html' , {"data":data})

class RecipeListView(ListView):
    model = Recipes
    template_name = "sandbox/index.html"
    context_object_name = "recipes"

class RecipeDetailView(DetailView):
    model = Recipes
    template_name = "sandbox/recipe_detail.html"
    context_object_name = "recipe"