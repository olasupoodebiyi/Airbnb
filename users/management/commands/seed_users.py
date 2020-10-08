from django.core.management.base import BaseCommand
from django_seed import Seed

# from rooms import models as room_models
from users.models import User


class Command(BaseCommand):

    help = "This commands creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users do you want?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Users Created!"))
