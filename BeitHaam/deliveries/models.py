from django.db import models
from django.contrib.auth.models import User
from dishes.models import Dish

# Create your models here.
class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_current = models.BooleanField(default=True)
    
class Items(models.Model):
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE)
    amount = models.IntegerField()

class Delivery(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,primary_key=True)
    is_delivered = models.BooleanField(null=True)
    address = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

