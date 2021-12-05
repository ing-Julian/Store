from django.db import models 
from .products import Products
from .bills import Bills
from .client import Client
from .user import User

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    prod_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    bill_id = models.ForeignKey(Bills, on_delete=models.SET_NULL, null=True)
    client_id = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    inventory = models.IntegerField(default=0)
