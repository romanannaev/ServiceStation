from django.shortcuts import render


# Create your views here.
from .models import *

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # # Генерация "количеств" некоторых главных объектов
    # num_books=Book.objects.all().count()
    # num_instances=BookInstance.objects.all().count()
    # # Доступные книги (статус = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    # num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.
    
    # # Отрисовка HTML-шаблона index.html с данными внутри 
    # # переменной контекста context
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