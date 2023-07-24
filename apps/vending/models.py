from django.db import models
from decimal import Decimal
from uuid import uuid4
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    class Meta:
        db_table = "product"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.name

class VendingMachineSlot(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], default=0)
    row = models.IntegerField(validators=[MaxValueValidator(9), MinValueValidator(1)])
    column = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])

    class Meta:
        db_table = "vending_machine_slot"
        unique_together = ('row', 'column')

# For simplicity we are going to keep the product stock/quantity on the VendingMachineSlot model 
# class Stock(models.Model):
#     product = models.OneToOneField("Product", unique=True, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     quantity = models.IntegerField(null=False, default=0, validators=[MinValueValidator(0)])
#     updated_at = models.DateTimeField(auto_now=True)
