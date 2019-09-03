from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
# Create your models here.

class Client(models.Model):
    """
    Model representing a client.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True )
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('client-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{}, {}'.format(self.last_name, self.first_name)
    

class ListOrders(models.Model):
    """
    Model representing a list of orders).
    """
    date = models.DateField(auto_now = False , auto_now_add = False)
    order_amount = models.CharField(max_length=8)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True) 
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)

    ORDER_STATUS = (
        ('f', 'Finished'),
        ('p', 'In Progress'),
        ('c', 'Cancelled'),
    )

    status = models.CharField(max_length=1, choices=ORDER_STATUS, blank=True, default='f', help_text='status order')

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('order-detail', args=[str(self.id)])

        
    def __str__(self):
        """
        String for representing the Model object
        """
        return '{} ({},{})'.format(self.id, self.client.last_name, self.client.first_name )

    class Meta:
        ordering = ["-date"]

class Car(models.Model):
    """
    Model representing a car.
    """
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    vin = models.CharField(max_length=200, null=True, blank=True )
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True) 

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('car-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{}({},{})'.format(self.make, self.client.last_name, self.client.first_name )

    class Meta:
        ordering = ["make"]