from django.db import models
from django.utils import timezone
import uuid

class Order(models.Model):
    name = models.CharField(max_length=300, verbose_name='name', help_text='name of order')
    quantity = models.IntegerField(help_text='quantity in order')
    price = models.DecimalField(max_digits=200, decimal_places=2)
    weigth = models.DecimalField(max_digits=200, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    
class Shipping(models.Model):
    STATUS = (
        ('pending', 'pendin'),
        ('shipping', 'shipped'),
    ) 
    id_inteface = models.UUIDField(default=uuid.uuid4)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    owner_name = models.CharField(max_length=300)
    owner_email = models.EmailField(max_length=300)
    shipment_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, choices=STATUS, default='pending')   