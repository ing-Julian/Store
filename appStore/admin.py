from django.contrib import admin
from .models.products import Products
from .models.client import Client
from .models.bills import Bills
from .models.sales import Sales
from .models.user import User

admin.site.register(Products)
admin.site.register(Client)
admin.site.register(Bills)
admin.site.register(Sales)
admin.site.register(User)


# Register your models here.
