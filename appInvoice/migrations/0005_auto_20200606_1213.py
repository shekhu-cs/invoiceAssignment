# Generated by Django 3.0.6 on 2020-06-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appInvoice', '0004_auto_20200605_1558'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
