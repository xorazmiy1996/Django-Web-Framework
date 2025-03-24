
from django import forms

from foodie_app.models import Category
from recipes.models import Recipes


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            "name": "Category name",
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['name', 'description', 'ingredients', 'directions', 'category']

