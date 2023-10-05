# Generated by Django 4.2.5 on 2023-10-04 18:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_orderproductcount_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproductcount',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, to='store.user', on_delete=django.db.models.deletion.CASCADE),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderproductcount',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order'),
            preserve_default=False,
        ),
    ]
