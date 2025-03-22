from django.db import models

from recipes.models import Recipes


# Create your models here.


class Comments(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

