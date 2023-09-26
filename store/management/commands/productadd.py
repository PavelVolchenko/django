from django.core.management.base import BaseCommand
from store.models import Product
import argparse


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument("-n", "--name", nargs="+", type=str, help="Input product name")
        parser.add_argument("-d", "--description", nargs="+", type=str, help="Input product description")
        parser.add_argument("-p", "--price", type=float, help="Input product price")

    def handle(self, *args, **kwargs):
        product = Product(
            product_name=' '.join(kwargs.get('name')),
            description=' '.join(kwargs.get('description')),
            price=kwargs.get('price'),
        )
        product.save()
        self.stdout.write(f"{product}\n+-- Product success added to database --")
