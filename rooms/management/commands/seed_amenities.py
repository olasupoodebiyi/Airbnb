from django.core.management.base import BaseCommand

# from rooms import models as room_models
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This commands says he loves me"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you i love you!"
    #     )

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon Monoxide Detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker in Room",
            "Cooking Hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double Bed",
            "Ensuite Bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair Dryer",
            "Heating",
            "Hot Tub",
            "Indoor Pool",
            "Ironing Board",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen-sized Bed",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke Detectors",
            "Sofa",
            "Stereo",
            "Swimming Pool",
            "Toilet",
            "Towels",
            "TV",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenties Created!"))
