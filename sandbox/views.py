from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from recipes.models import Recipes
from sandbox.forms import FeedbackForm
from django.contrib import messages


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
def thank_you(request):
    return HttpResponse("thank-you-url")
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, "Feedback sent successfully!")
            return redirect("sandbox:index")
    else:
        form = FeedbackForm()
    return render(request, "sandbox/feedback_form.html", {"form": form})

