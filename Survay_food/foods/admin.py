from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Food)

def __str__(self):
    name = models.Food.name