from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500)

class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=500)
    is_gluten_free = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Topping(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=500)