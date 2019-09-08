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
#added client forms
urlpatterns += [  
    url(r'^client/create/$', views.ClientCreate.as_view(), name='client_create'),
    url(r'^client/(?P<pk>\d+)/update/$', views.ClientUpdate.as_view(), name='client_update'),
    url(r'^client/(?P<pk>\d+)/delete/$', views.ClientDelete.as_view(), name='client_delete'),
]
#added car forms
urlpatterns += [  
    url(r'^car/create/$', views.CarCreate.as_view(), name='car_create'),
    url(r'^car/(?P<pk>\d+)/update/$', views.CarUpdate.as_view(), name='car_update'),
    url(r'^car/(?P<pk>\d+)/delete/$', views.CarDelete.as_view(), name='car_delete'),
]
#added orders forms
urlpatterns += [  
    url(r'^order/create/$', views.OrderCreate.as_view(), name='order_create'),
    url(r'^order/(?P<pk>\d+)/update/$', views.OrderUpdate.as_view(), name='order_update'),
    url(r'^order/(?P<pk>\d+)/delete/$', views.OrderDelete.as_view(), name='order_delete'),
]
