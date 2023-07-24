from _decimal import Decimal
from datetime import datetime

import factory
from factory import Faker
from factory.django import DjangoModelFactory
from apps.vending.models import Product, VendingMachineSlot


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    id = Faker("uuid4")
    name = "Snickers Bar"
    price = Decimal("10.40")
    created_at = datetime(2023, 5, 30, 12)
    updated_at = datetime(2023, 5, 30, 23)

class VendingMachineSlotFactory(DjangoModelFactory):
    class Meta:
        model = VendingMachineSlot

    id = Faker("uuid4")
    quantity = 1
    product = factory.SubFactory(ProductFactory)
    row = 1
    column = 3