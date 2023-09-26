from django.core.management.base import BaseCommand
from store.models import User


class Command(BaseCommand):
    help = "Get user at ID or show all users if entered ID = 0."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        id = kwargs["id"]
        if id == 0:
            users = User.objects.all()
            for user in users:
                self.stdout.write(f'{user}')
        else:
            user = User.objects.get(id=id)
            self.stdout.write(f'{user}')