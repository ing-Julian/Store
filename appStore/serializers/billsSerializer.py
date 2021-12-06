from appStore.models.bills import Bills
from rest_framework import serializers

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ['date', 'total']
