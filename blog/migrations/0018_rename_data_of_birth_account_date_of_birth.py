# Generated by Django 4.2.2 on 2023-08-10 07:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0017_account"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account",
            old_name="data_of_birth",
            new_name="date_of_birth",
        ),
    ]
