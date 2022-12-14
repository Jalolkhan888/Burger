# Generated by Django 4.1.2 on 2022-10-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("burger", "0002_chef_client_alter_book_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="is_published"),
        ),
        migrations.AddField(
            model_name="chef",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="is_published"),
        ),
        migrations.AddField(
            model_name="client",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="is_published"),
        ),
        migrations.AlterField(
            model_name="food",
            name="image",
            field=models.ImageField(upload_to="media/foods/", verbose_name="Photo"),
        ),
    ]
