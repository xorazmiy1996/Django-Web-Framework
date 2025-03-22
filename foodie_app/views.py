from django.shortcuts import render

from .forms import CategoryForm
from .models import Category
from recipes.models import Recipes

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'foodie_app/index.html', {'categories': categories})

def recipes(request, category_id):
    recipes = Recipes.objects.filter(category_id=category_id)
    category = Category.objects.get(id=category_id)
    return render(request, 'foodie_app/recipes.html', {'recipes': recipes, 'category': category})

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        return render(request, 'foodie_app/add_category.html')
    else:
        form = CategoryForm()
        return render(request, 'foodie_app/add_category.html', {'form': form})