from django.contrib import admin
from .models import Client, Car, Order
# Register your models here.

admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Order)

