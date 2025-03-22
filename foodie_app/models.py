from symtable import Class

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name = "Kategoriyalar1"
        verbose_name_plural = "Kategoriyar2"

    def __str__(self):
        return self.name


