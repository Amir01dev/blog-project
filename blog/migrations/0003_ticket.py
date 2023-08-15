# Generated by Django 4.2.2 on 2023-07-17 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_options_alter_post_author_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField(verbose_name="پیام")),
                (
                    "name",
                    models.CharField(max_length=250, verbose_name="نام و نام خانوادگی"),
                ),
                ("phone", models.CharField(max_length=11, verbose_name="شماره تلفن")),
                ("email", models.EmailField(max_length=250, verbose_name="ایمیل")),
                ("subject", models.CharField(max_length=250, verbose_name="موضوع")),
            ],
            options={
                "verbose_name": "تیکت",
                "verbose_name_plural": "تیکت ها",
            },
        ),
    ]