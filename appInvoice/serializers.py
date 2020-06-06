from rest_framework import serializers
from .models import InvoiceModel


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceModel
        # fields = ['invoiceNumber', 'deuDate', 'orderNumber', 'invoiceDate', 'total', 'status']
        fields = '__all__'
