from django.core.management.base import BaseCommand
from store.models import User


class Command(BaseCommand):
    help = "Get user at ID or show all users if entered ID = 0."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        if pk == 0:
            users = User.objects.filter().all()
            for user in users:
                self.stdout.write(f'{user}')
        else:
            user = User.objects.filter(pk=pk).first()
            self.stdout.write(f'{user}')