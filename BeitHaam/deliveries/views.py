from django.shortcuts import render,redirect
from dishes.models import Category,Dish
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from deliveries.models import Cart,Items,Delivery
from main.forms import SubmitDelivery


# Create your views here.

def menu(request):
    cats = Category.objects.all()
    dishes = Dish.objects.all()
    return render(request,'menu.html',{"dishes":dishes,"cats":cats})

@login_required
def cart(request):
        if Cart.objects.filter(user_id = request.user, is_current=True).exists():
            current_cart = Cart.objects.get(user_id = request.user,is_current=True)
            items = Items.objects.filter(cart_id=current_cart)
            total = 0
            for x in items:
                total = total + (x.amount*x.dish_id.price)
            return render(request,'cart.html',{"items":items,"total":total,"cart_id":current_cart.id})
        return render(request,'cart.html',{})


@login_required
def add_to_cart(request,id):
    user = User.objects.get(pk=request.user.id)
    try:
        active_cart = Cart.objects.get(user_id = user, is_current = True)
    except:
        active_cart = Cart(user_id = user)    
        active_cart.save()
    if request.method == "POST":
        amount = request.POST.get('amount')
        dish = Dish.objects.get(pk=id)
        item = Items(dish_id = dish, cart_id = active_cart, amount = amount)
        item.save()
    return redirect('menu')

@login_required
def remove_from_cart(request,id):
    item = Items.objects.get(pk=id)
    item.delete()
    return redirect('cart')

@login_required
def checkout(request,id):

    cart = Cart.objects.get(pk=id)
    if request.method == "POST":
        form = SubmitDelivery(request.POST)
        if form.is_valid():
            street = form.cleaned_data["street"]
            house_number = form.cleaned_data["house_number"]
            city = form.cleaned_data["city"]
            comment = form.cleaned_data["comment"]
            address = street+" "+str(house_number)+", "+city
            d = Delivery(cart_id=cart,address=address,comment=comment)
            d.save()
            cart.is_current = False
            cart.save()
            return redirect('thankyou', id=cart.id)
    else:
        form = SubmitDelivery()
    return render(request,'checkout.html',{"form":form,"cart":cart})
 
@login_required
def thankyou(request,id):
    delivery = Delivery.objects.get(pk=id)
    cart = Cart.objects.get(pk=id)
    items = Items.objects.filter(cart_id=cart)
    total = 0
    for x in items:
        total = total + (x.amount*x.dish_id.price)


    return render(request,'thankyou.html',{"delivery":delivery,"total":total})
