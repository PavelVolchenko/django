# Generated by Django 4.2.5 on 2023-10-03 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]
