# Generated by Django 4.1.2 on 2023-06-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_alter_profile_otp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="otp",
            field=models.CharField(max_length=6),
        ),
    ]
