from django.shortcuts import render

from recipes.models import Recipes


# Create your views here.

def recipes(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

def recipe(request, recipe_id):
    recipe = Recipes.objects.get(id=recipe_id)
    return render(request, "recipes/"
                           "recipe.html", {'recipe': recipe})
