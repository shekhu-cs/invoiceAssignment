from django.db import models


class InvoiceModel(models.Model):
    invoiceNumber = models.CharField(max_length=15)
    deuDate = models.CharField(max_length=25)
    orderNumber = models.CharField(max_length=15)
    invoiceDate = models.CharField(max_length=25)
    total = models.CharField(max_length=15)
    status = models.CharField(max_length=30)
