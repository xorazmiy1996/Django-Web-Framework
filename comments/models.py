from django.contrib.auth.models import User
from django.db import models

from recipes.models import Recipes




# Create your models here.


class Comments(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, related_name='comments')
    text = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.recipe.name}"

