from django.core.management.base import BaseCommand
from store.models import User
import argparse


class Command(BaseCommand):
    help = "Create user. Input username, email, password through space."

    def add_arguments(self, parser):
        parser.add_argument("args", nargs='+', type=str, help="username email password")

    def handle(self, *args, **kwargs):
        user = User(username=args[0], email=args[1], password=args[2])
        user.save()
        self.stdout.write(f"{user}\n+-- Product success added to database --")
