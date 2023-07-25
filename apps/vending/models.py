from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from decimal import Decimal
from uuid import uuid4
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.name
    
    class Meta:
        db_table = "product"

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

class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        """
        Creates and saves a User with the the given username and password.
        """
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    username = models.CharField(max_length=120, unique=True)
    balance = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))], default=Decimal("0.00"))

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
