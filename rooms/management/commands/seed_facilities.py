from django.core.management.base import BaseCommand

# from rooms import models as room_models
from rooms.models import Facility


class Command(BaseCommand):

    help = "This commands says he loves me"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you i love you!"
    #     )

    def handle(self, *args, **options):
        facilities = [
            "Private Entrance",
            "Paid Parking on Premises",
            "Paid Parking off Premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities Created!"))
