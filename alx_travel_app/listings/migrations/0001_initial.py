# Generated by Django 5.2.4 on 2025-07-13 17:54

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Listing",
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
                    "title",
                    models.CharField(help_text="Title of the listing", max_length=200),
                ),
                (
                    "description",
                    models.TextField(help_text="Detailed description of the listing"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Price per night",
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0.01)],
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        help_text="Location of the listing", max_length=200
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether the listing is active"
                    ),
                ),
                (
                    "host",
                    models.ForeignKey(
                        help_text="Host of the listing",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="listings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Travel Listing",
                "verbose_name_plural": "Travel Listings",
                "ordering": ["-created_at"],
            },
        ),
    ]
