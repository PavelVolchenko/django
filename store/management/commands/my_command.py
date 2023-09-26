from django.core.management.base import BaseCommand
from store.models import User


class Command(BaseCommand):
    help = "Hello"

    def handle(self, *args, **kwargs):
        self.stdout.write("Hello and you are welcome in my website!")
