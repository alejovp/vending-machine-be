from _decimal import Decimal
from uuid import UUID

from apps.vending.models import Product
from apps.vending.tests.factories import ProductFactory
import pytest


# This annotation (see more in section 3) is required because factories 
# inheriting from DjangoModelFactory will be stored in the db. 
# You can prevent this by calling the .build() method instead of 
# the constructor (ProductFactory.build(name="Heidi chocolate"))
@pytest.mark.django_db
def test_product_creation():
    test_product_name = "Heidi chocolate"
    test_product_price = Decimal("5.32")
    test_product = ProductFactory(name=test_product_name, price=test_product_price)

    stored_product = Product.objects.get(id=test_product.id)

    # assert stored_product == test_product
    assert stored_product.price == test_product_price
    assert stored_product.name == test_product_name