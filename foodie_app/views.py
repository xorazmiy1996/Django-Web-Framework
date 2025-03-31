from django.shortcuts import render, redirect, get_object_or_404

from .forms import CategoryForm, RecipeForm
from .models import Category
from recipes.models import Recipes
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'foodie_app/index.html', {'categories': categories})

def recipes(request, category_id):
    recipes = Recipes.objects.filter(category_id=category_id)
    category = Category.objects.get(id=category_id)
    return render(request, 'foodie_app/recipes.html', {'recipes': recipes, 'category': category})
@login_required
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("foodie_app:add-category-ulr")
        else:
            return render(request, 'foodie_app/add_category.html', {'form': form})
    else:
        form = CategoryForm()
        return render(request, 'foodie_app/add_category.html', {'form': form})

# def add_recipe(request):
#     if request.method == "POST":
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("recipes:index")
#     else:
#         form = RecipeForm()
#     return render(request, "foodie_app/add_recipe.html", {'form': form})

def add_recipe(request, category_id=None):
    category = None
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        form = RecipeForm(request.POST or None,files=request.FILES,initial={"category": category})
    else:
        form = RecipeForm(request.POST or None,files=request.FILES)
    if request.method == "POST" and form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.user = request.user
        new_recipe.save()
        return redirect("recipes:recipes_ulr")

    return render(request, "foodie_app/add_recipe.html", {'form': form})