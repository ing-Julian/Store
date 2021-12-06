from rest_framework import serializers
from appStore.models.sales import Sales
from appStore.models.user import User
from appStore.models.bills import Bills
from appStore.models.client import Client
from appStore.models.products import Products

# from appStore.serializers.salesSerializer import SalesSerializer

class SalesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sales
        fields = ['id', 'prod_id', 'bill_id', 'user_id', 'user_id','quantity']

    