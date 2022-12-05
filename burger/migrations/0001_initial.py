# Generated by Django 4.1.2 on 2022-10-26 15:30

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=200, verbose_name="Surname")),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("date", models.DateField(blank=True)),
                ("time", models.TimeField(blank=True)),
                ("guest", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(max_length=250, verbose_name="Category Name"),
                ),
                ("url", models.SlugField(max_length=250, verbose_name="URL")),
                ("description", models.TextField(verbose_name="Description")),
            ],
            options={"verbose_name": "Category", "verbose_name_plural": "Categories",},
        ),
        migrations.CreateModel(
            name="Food",
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
                ("title", models.CharField(max_length=250, verbose_name="Name")),
                (
                    "url",
                    models.SlugField(max_length=250, unique=True, verbose_name="URL"),
                ),
                ("description", models.TextField(verbose_name="Description")),
                ("image", models.ImageField(upload_to="foods/", verbose_name="Photo")),
                (
                    "time_create",
                    models.DateTimeField(auto_now_add=True, verbose_name="time_create"),
                ),
                (
                    "time_update",
                    models.DateTimeField(auto_now=True, verbose_name="time_update"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="is_published"),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        default=0, help_text="show dollar", verbose_name="Price"
                    ),
                ),
                (
                    "cat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="burger.category",
                        verbose_name="category",
                    ),
                ),
            ],
            options={"verbose_name": "Food", "verbose_name_plural": "Foods",},
        ),
    ]