# Generated by Django 4.2.2 on 2023-07-21 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending', '0008_alter_stock_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2023, 7, 21, 15, 16, 24, 220286, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
