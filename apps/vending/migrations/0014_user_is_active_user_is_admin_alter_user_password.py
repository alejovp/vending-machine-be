# Generated by Django 4.2.2 on 2023-07-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending', '0013_user_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
