# Generated by Django 4.1.2 on 2022-10-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("burger", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Chef",
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
                (
                    "position",
                    models.CharField(
                        help_text="position in job",
                        max_length=100,
                        verbose_name="Position",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="media/chefs", verbose_name="Photo"),
                ),
            ],
            options={"verbose_name": "Chef", "verbose_name_plural": "Chefs",},
        ),
        migrations.CreateModel(
            name="Client",
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
                ("name", models.CharField(max_length=200, verbose_name="Fullname")),
                (
                    "profession",
                    models.CharField(max_length=100, verbose_name="Profession"),
                ),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(upload_to="media/clients", verbose_name="Photo"),
                ),
            ],
            options={"verbose_name": "Client", "verbose_name_plural": "Clients",},
        ),
        migrations.AlterModelOptions(
            name="book",
            options={"verbose_name": "Order", "verbose_name_plural": "Orders"},
        ),
    ]
