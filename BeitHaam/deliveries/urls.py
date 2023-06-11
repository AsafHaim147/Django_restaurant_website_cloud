from django.urls import path
from deliveries import views

urlpatterns = [
path('menu',views.menu,name="menu"),
path('cart',views.cart,name="cart"),
path('add_to_cart/<int:id>',views.add_to_cart,name="add_to_cart"),
path('remove_from_cart/<int:id>',views.remove_from_cart,name="remove_from_cart"),
path('checkout/<int:id>',views.checkout,name="checkout"),
path('thankyou/<int:id>',views.thankyou,name="thankyou")
]