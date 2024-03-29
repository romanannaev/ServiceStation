from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
# Create your models here.


class Client(models.Model):
    """
    Model representing a client.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('client-detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('client_update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('client_delete', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{}, {}'.format(self.last_name, self.first_name)


class Order(models.Model):
    """
    Model representing a list of orders).
    """
    date = models.DateField(auto_now=False, auto_now_add=False)
    order_amount = models.CharField(max_length=8)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)

    ORDER_STATUS = (
        ('f', 'Finished'),
        ('p', 'In Progress'),
        ('c', 'Cancelled'),
    )

    status = models.CharField(max_length=1, choices=ORDER_STATUS,
                              blank=True, default='f', help_text='status order')

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('order-detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('order_update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('order_delete', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{} ({},{})'.format(self.id, self.client.last_name, self.client.first_name)

    class Meta:
        ordering = ["-date"]


class Car(models.Model):
    """
    Model representing a car.
    """
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    vin = models.CharField(max_length=200, null=True, blank=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('car-detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('car_update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('car_delete', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{}({},{})'.format(self.make, self.client.last_name, self.client.first_name)

    class Meta:
        ordering = ["make"]


class OrderApplication(models.Model):
    """
    Model representing a order application.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, null=True, blank=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular application instance.
        """
        return reverse('application_detail', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('application_delete', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{}, {}({})'.format(self.last_name, self.first_name, self.date_pub)

    class Meta:
        ordering = ["-date_pub"]
