from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .models import Client, Car, Order, OrderApplication
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import *


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(
        request,
        'main_index.html',
    )


def get_grateful(request):
    return render(
        request,
        'grateful_application.html',
    )


class ClientListView(generic.ListView):
    model = Client


class ClientDetailView(generic.DetailView):
    context_object_name = 'model'
    model = Client


class CarListView(generic.ListView):
    model = Car


class CarDetailView(generic.DetailView):
    context_object_name = 'model'
    model = Car


class OrderListView(generic.ListView):
    model = Order


class OrderDetailView(generic.DetailView):
    context_object_name = 'model'
    model = Order


class OrderApplicationListView(generic.ListView):
    model = OrderApplication


class OrderApplicationDetailView(generic.DetailView):
    context_object_name = 'model'
    model = OrderApplication

    
# added Client forms


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = '__all__'
    initial = {'date_of_birth': '20/02/1992', }


class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['first_name', 'last_name',
              'date_of_birth', 'address', 'phone', 'email']


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients')
    raise_exception = True

# added Car forms


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = '__all__'


class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = '__all__'


class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = reverse_lazy('cars')
    raise_exception = True

# added Order forms


class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    fields = '__all__'


class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    fields = '__all__'


class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('orders')
    raise_exception = True

# added forms order application


class OrderApplicationCreate(CreateView):
    model = OrderApplication
    fields = ['first_name', 'last_name', 'phone']
    success_url = reverse_lazy('grateful')


class OrderApplicationDelete(LoginRequiredMixin, DeleteView):
    model = OrderApplication
    success_url = reverse_lazy('applications')
    raise_exception = True
