# Generated by Django 4.1.2 on 2022-10-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("burger", "0007_alter_book_date_alter_book_is_published_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="time",
            field=models.CharField(max_length=200, verbose_name="Time"),
        ),
    ]
