from django.shortcuts import render


# Create your views here.
from .models import *

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(
        request,
        'index.html',
    )

from django.views import generic

class ClientListView(generic.ListView):
    model = Client

class ClientDetailView(generic.DetailView):
    model = Client


class CarListView(generic.ListView):
    model = Car


class CarDetailView(generic.DetailView):
    model = Car


class OrderListView(generic.ListView):
    model = Order


class OrderDetailView(generic.DetailView):
    model = Order

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client, Car, Order

#added Client forms
class ClientCreate(CreateView):
    model = Client
    fields = '__all__'
    initial={'date_of_birth':'20/02/1992',}

class ClientUpdate(UpdateView):
    model = Client
    fields = ['first_name','last_name','date_of_birth','address', 'phone', 'email']

class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('clients')

#added Car forms 
class CarCreate(CreateView):
    model = Car
    fields = '__all__'

class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('cars')

#added Order forms 
class OrderCreate(CreateView):
    model = Order
    fields = '__all__'

class OrderUpdate(UpdateView):
    model = Order
    fields = '__all__'

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders')
