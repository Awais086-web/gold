# Generated by Django 4.1.2 on 2023-06-20 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0016_profile_address_profile_phone"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="phone",
            new_name="phone_number",
        ),
    ]
