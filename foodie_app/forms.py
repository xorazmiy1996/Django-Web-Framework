
from django import forms

from foodie_app.models import Category
from recipes.models import Recipes


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }



class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['name', 'description', 'ingredients', 'directions', 'category','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
            'directions': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}),

        }

