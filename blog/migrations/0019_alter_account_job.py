# Generated by Django 4.2.2 on 2023-08-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0018_rename_data_of_birth_account_date_of_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="job",
            field=models.CharField(max_length=250, verbose_name="شغل"),
        ),
    ]
