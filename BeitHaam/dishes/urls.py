from django.urls import path
from dishes import views

urlpatterns = [
    path('add_dish',views.add_dish,name="add_dish"),
    path('edit_dish/<int:id>',views.edit_dish,name="edit_dish"),
    path('delete_dish/<int:id>',views.delete_dish,name="delete_dish"),
    path('dishes',views.dishes,name="dishes"),
    path('add_category',views.add_category,name="add_category"),
    path('edit_category/<int:id>',views.edit_category,name="edit_category"),
    path('delete_category/<int:id>',views.delete_category,name="delete_category"),
    path('categories',views.categories,name="categories"),
    path('add_topping',views.add_topping,name="add_topping"),
    path('edit_topping/<int:id>',views.edit_topping,name="edit_topping"),
    path('delete_topping/<int:id>',views.delete_topping,name="delete_topping"),
    path('toppings',views.toppings,name="toppings"),
]