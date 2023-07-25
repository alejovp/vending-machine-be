# Generated by Django 4.2.2 on 2023-07-25 13:36

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vending', '0011_alter_product_name_alter_vendingmachineslot_column_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vendingmachineslot',
            unique_together={('row', 'column')},
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=4, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
