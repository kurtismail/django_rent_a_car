# Generated by Django 4.1.5 on 2023-01-28 06:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0003_resevation_user_rent_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resevation',
            new_name='Reservation',
        ),
    ]