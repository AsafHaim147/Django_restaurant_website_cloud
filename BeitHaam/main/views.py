from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from deliveries.models import Cart,Delivery,Items
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from main.forms import SignUpForm

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard/%d'%request.user.id,{"id":request.user.id})
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard/%d'%request.user.id,{"id":request.user.id})
            else:
                print("login error")
        else:
            return render(request,'registration/login.html')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard/%d'%request.user.id,{"id":request.user.id})
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            return redirect('dashboard')
    return render(request,'registration/register.html',{'form':form})

@login_required
def show_dashboard(request):
    user = User.objects.get(id=request.user.id)
    return render(request,'userdashboard.html', {"user":user})

@login_required
def edit_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = SignUpForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request,current_user)
            return redirect('userdashboard')

    return render(request,'edit_user.html',{'form':form})

def main(request):
    return render(request,'main.html')

@login_required
def userdashboard(request):
    if request.user.is_authenticated:
        return redirect('dashboard/')

@login_required
def manage_staff(request):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    users = User.objects.exclude(pk=request.user.id)
    return render(request,'manage_staff.html',{"users":users})

@login_required
def change_staff_status(request,id):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    user = User.objects.get(pk=id)
    if user.is_staff:
        user.is_staff = False
        user.save()
    else:
        user.is_staff = True
        user.save()
    return redirect('manage_staff')

@login_required
def view_orders(request):
    orders = Cart.objects.filter(user_id=request.user)
    return render(request,'orders.html',{"orders":orders})

@login_required
def view_order(request,id):
    items = Items.objects.filter(cart_id=id)
    total = 0
    for x in items:
        total = total + (x.amount*x.dish_id.price)
    return render(request,'view_order.html',{"items":items,"cart_id":id,"total":total})

@login_required
def manage_deliveries(request):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    deliveries = Delivery.objects.all()
    return render(request,'manage_deliveries.html',{"deliveries":deliveries})

@login_required
def delivery_failed(request,id):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    delivery = Delivery.objects.get(pk=id)
    delivery.is_delivered = False
    delivery.save()
    return redirect('manage_deliveries')

@login_required
def delivery_completed(request,id):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    delivery = Delivery.objects.get(pk=id)
    delivery.is_delivered = True
    delivery.save()
    return redirect('manage_deliveries')

