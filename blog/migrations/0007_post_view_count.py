# Generated by Django 4.2.2 on 2023-07-22 08:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_post_reading_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="view_count",
            field=models.IntegerField(default=0, verbose_name="تعداد بازدید"),
        ),
    ]