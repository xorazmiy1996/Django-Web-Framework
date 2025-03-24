from django.shortcuts import render, get_object_or_404, redirect

from foodie_app.forms import RecipeForm
from foodie_app.models import Category
from recipes.models import Recipes
from foodie_app.forms import RecipeForm

# Create your views here.

def recipes(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

def recipe(request, recipe_id):
    recipe = Recipes.objects.get(id=recipe_id)
    return render(request, "recipes/"
                           "recipe.html", {'recipe': recipe})



def add_recipe(request, category_id=None):
    category = None
    if category_id:
        # category = Category.objects.get(id=category_id)
        category = get_object_or_404(Category, id=category_id)
        form = RecipeForm(request.POST or None, initial={"category": category})
    else:
        form = RecipeForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_recipe = form.save(commit=True)
        return redirect("foodie_app:recipes", category_id=new_recipe.category.id)

    render(request, 'recipes/add_recipe.html', {'form': form, 'category': category})



