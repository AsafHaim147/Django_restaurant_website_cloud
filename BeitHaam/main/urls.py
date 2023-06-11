from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('login',views.login_user,name="login"),
    path('register',views.register_user,name="register"),
    path('userdashboard',views.userdashboard,name="userdashboard"),
    path('dashboard/',views.show_dashboard,name="dashboard"),
    path('edit_user',views.edit_user,name="edit_user"),
    path('manage_staff',views.manage_staff,name="manage_staff"),
    path('manage_deliveries',views.manage_deliveries,name="manage_deliveries"),
    path('view_orders',views.view_orders,name="view_orders"),
    path('view_order/<int:id>',views.view_order,name="view_order"),
    path('delivery_failed/<int:id>',views.delivery_failed,name="delivery_failed"),
    path('delivery_completed/<int:id>',views.delivery_completed,name="delivery_completed"),
    path('change_staff_status/<int:id>',views.change_staff_status,name="change_staff_status")
    
]