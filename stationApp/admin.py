from django.contrib import admin
from .models import Client, Car, ListOrders
# Register your models here.

admin.site.register(Client)
admin.site.register(Car)
admin.site.register(ListOrders)

