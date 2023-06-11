from django.shortcuts import render,redirect
from main import forms
from dishes.models import Category,Dish,Topping
from django.contrib.auth.decorators import login_required

# Create your views here.

### DISH VIEWS ###
@login_required
def add_dish(request):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    if request.method == "POST":
        form = forms.AddNewDish(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            price = form.cleaned_data["price"]
            image = form.cleaned_data["image"]
            description = form.cleaned_data["description"]
            is_gluten_free = form.cleaned_data["is_gluten_free"]
            is_vegan = form.cleaned_data["is_vegan"]
            category = Category.objects.get(id=int(request.POST["category"]))
            d = Dish(name=name,price=price,image=image,description=description,
                     is_gluten_free=is_gluten_free,is_vegan=is_vegan,category=category)
            d.save()
            return redirect('dishes') 
    else:
        cats = Category.objects.all()
        form = forms.AddNewDish()
    return render(request,'dishes/add_dish.html',{"cats":cats,"form":form})

@login_required
def edit_dish(request,id):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    cats = Category.objects.all()
    dish = Dish.objects.get(id=id)
    if request.method == "POST":
        form = forms.AddNewDish(request.POST)
        if form.is_valid():
            dish.name = form.cleaned_data["name"]
            dish.price = form.cleaned_data["price"]
            dish.image = form.cleaned_data["image"]
            dish.description = form.cleaned_data["description"]
            dish.is_gluten_free = form.cleaned_data["is_gluten_free"]
            dish.is_vegan = form.cleaned_data["is_vegan"]
            dish.category = Category.objects.get(id=int(request.POST["category"]))
            dish.save()
            return redirect('dishes')
    else:
        form = forms.AddNewDish(initial={"name":dish.name,"price":dish.price,"image":dish.image,
                                             "description":dish.description,"is_gluten_free":dish.is_gluten_free,
                                             "is_vegan":dish.is_vegan,"category":dish.category})
    return render(request,'dishes/edit_dish.html',{"form":form,"dish":dish,"id":dish.id,"cats":cats})

@login_required
def delete_dish(request,id):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    dish = Dish.objects.get(pk=id)
    dish.delete()
    return redirect('dishes')

@login_required
def dishes(request):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    dishes = Dish.objects.all()
    return render(request,'dishes/dishes.html',{"dishes":dishes})

### CATEGORY VIEWS ###

@login_required
def add_category(request):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    if request.method == "POST":
        form = forms.AddNewCategory(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            image = form.cleaned_data["image"]
            c = Category(name=name,image=image)
            c.save()
            return redirect('categories') 
    else:
        form = forms.AddNewCategory()
    return render(request,'categories/add_category.html',{"form":form})

@login_required
def edit_category(request,id):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    cat = Category.objects.get(id=id)
    if request.method == "POST":
        form = forms.AddNewCategory(request.POST)
        if form.is_valid():
            cat.name = form.cleaned_data["name"]
            cat.image = form.cleaned_data["image"]
            cat.save()
            return redirect('categories')
    else:
        form = forms.AddNewCategory(initial={"name":cat.name,"image":cat.image})
    return render(request,'categories/edit_category.html',{"form":form,"id":cat.id})

@login_required
def delete_category(request,id):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    cat = Category.objects.get(pk=id)
    cat.delete()
    return redirect('categories')

@login_required
def categories(request):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    cats = Category.objects.all()
    return render(request,'categories/categories.html',{"cats":cats})

### TOPPING VIEWS ###

@login_required
def add_topping(request):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    if request.method == "POST":
        form = forms.AddNewTopping(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            price = form.cleaned_data["price"]
            image = form.cleaned_data["image"]
            t = Topping(name=name,price=price,image=image)
            t.save()
            return redirect('toppings') 
    else:
        form = forms.AddNewTopping()
    return render(request,'toppings/add_topping.html',{"form":form})

@login_required
def edit_topping(request,id):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    top = Topping.objects.get(id=id)
    if request.method == "POST":
        form = forms.AddNewTopping(request.POST)
        if form.is_valid():
            top.name = form.cleaned_data["name"]
            top.price = form.cleaned_data["price"]
            top.image = form.cleaned_data["image"]
            top.save()
            return redirect('toppings')
    else:
        form = forms.AddNewTopping(initial={"name":top.name,"price":top.price,"image":top.image})
    return render(request,'toppings/edit_topping.html',{"form":form,"id":top.id})

@login_required
def delete_topping(request,id):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    top = Topping.objects.get(pk=id)
    top.delete()
    return redirect('toppings')

@login_required
def toppings(request):
    if request.user.is_staff == False:
        return redirect('userdashboard')
    tops = Topping.objects.all()
    return render(request,'toppings/toppings.html',{"tops":tops})

