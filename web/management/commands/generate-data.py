import random

import faker.providers
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from faker import Faker
from djmoney.money import Money
from web.models import GoodCard, GoodCategory

CATEGORIES = [
    "Sofa",
    "Bed",
    "Wardrobe",
]
MIN_MONEY = 50
MAX_MONEY = 2000
MIN_INDEX = 1
MAX_INDEX = 8

class Provider(faker.providers.BaseProvider):
    def ecomerce_category(self):
        return self.random_element(CATEGORIES)


class Command(BaseCommand):
    help = "Command info"

    def handle(self, *args, **options):
        amount = 1
        if options['amount']:
            amount = options['amount']
        fake = Faker('en-GB')
        fake.add_provider(Provider)
        for _ in range(amount):
            category = fake.ecomerce_category()
            name = fake.unique.first_name()

            cat_id = GoodCategory.objects.get(title=category).id

            image_number = random.randint(MIN_INDEX, MAX_INDEX)
            money = random.randint(MIN_MONEY, MAX_MONEY)

            image_path = 'images/' + category + '/' + category + str(image_number) + '.jpeg'

            temp = GoodCard.objects.create(title=name, category_id=cat_id, price=Money(money ,'USD'))
            temp.image = ImageFile(open(image_path, "rb"))
            temp.save()
        self.stdout.write(self.style.SUCCESS(f"Amount of generated goods: {amount}"))

    def add_arguments(self, parser):
        parser.add_argument(
            'amount', type=int
        )
