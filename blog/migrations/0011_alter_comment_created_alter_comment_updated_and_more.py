# Generated by Django 4.2.2 on 2023-07-24 06:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_alter_comment_created_alter_comment_updated_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش"),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="publish",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="تاریخ انتشار"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
