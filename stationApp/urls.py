from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clients/$', views.ClientListView.as_view(), name='clients'),
    url(r'^client/(?P<pk>\d+)$', views.ClientDetailView.as_view(), name='client-detail'),
    url(r'^cars/$', views.CarListView.as_view(), name='cars'),
    url(r'^car/(?P<pk>\d+)$', views.CarDetailView.as_view(), name='car-detail'),
    url(r'^orders/$', views.OrderListView.as_view(), name='orders'),
    url(r'^order/(?P<pk>\d+)$', views.OrderDetailView.as_view(), name='order-detail'),
]
