# Generated by Django 4.2.5 on 2023-10-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_orderproductcount_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='order_products', through='store.OrderProductCount', to='store.product'),
        ),
        migrations.AlterField(
            model_name='orderproductcount',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
