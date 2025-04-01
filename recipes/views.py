from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from comments.forms import CommentForm
from foodie_app.models import Category
from recipes.forms import SearchForm
from recipes.models import Recipes
from foodie_app.forms import RecipeForm

# Create your views here.

def recipes(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    # recipe = Recipes.objects.get(id=recipe_id)
    recipe = get_object_or_404(Recipes, id=recipe_id)
    comments = recipe.comments.all()

    new_comment = None


    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.user = request.user
            new_comment.save()
            return redirect(recipe.get_absolute_url())
    else:
        comment_form = CommentForm()




    return render(request, "recipes/"
                           "recipe.html", {'recipe': recipe, 'comments':comments, 'comment_form': comment_form})



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

def search_results(request):
    form = SearchForm(request.GET)   # request.GET ni to'g'ridan-to'g'ri berish
    query = form.data.get("query", "")  # form dan query ni olish
    results = Recipes.objects.filter(name__icontains=query) if query else []
    context = {'results': results, 'query': query}
    return render(request, 'recipes/search_results.html', context)

@login_required
def toggle_favorite(request, recipe_id):
    print(recipe_id)
    recipe = get_object_or_404(Recipes, id=recipe_id)
    if request.user in recipe.favorited_by.all():
        recipe.favorited_by.remove(request.user)
    else:
        recipe.favorited_by.add(request.user)
    return redirect("recipes:recipe_detail_ulr", recipe_id=recipe_id)

