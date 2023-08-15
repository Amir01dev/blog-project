# Generated by Django 4.2.2 on 2023-07-24 06:48

from django.db import migrations
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0011_alter_comment_created_alter_comment_updated_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created",
            field=django_jalali.db.models.jDateTimeField(
                auto_now_add=True, verbose_name="تاریخ ایجاد"
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="updated",
            field=django_jalali.db.models.jDateTimeField(
                auto_now=True, verbose_name="تاریخ ویرایش"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="publish",
            field=django_jalali.db.models.jDateTimeField(
                default=django.utils.timezone.now, verbose_name="تاریخ انتشار"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="updated",
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
    ]