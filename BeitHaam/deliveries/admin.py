from django.contrib import admin
from deliveries.models import Items,Cart,Delivery

# Register your models here.
admin.site.register(Items)
admin.site.register(Cart)
admin.site.register(Delivery)