# Generated by Django 5.1.2 on 2024-10-24 23:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "final_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("image", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("discount", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "has_rebate",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                ("chair_type", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("processed", "Processed"),
                            ("shipped", "Shipped"),
                            ("delivered", "Delivered"),
                            ("canceled", "Canceled"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "order_number",
                    models.CharField(editable=False, max_length=6, unique=True),
                ),
                (
                    "order_creation_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "customer_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("card_number", models.CharField(blank=True, max_length=16, null=True)),
                ("card_exp", models.CharField(blank=True, max_length=5, null=True)),
                ("cvv", models.CharField(blank=True, max_length=3, null=True)),
                ("shipping_address", models.TextField(blank=True, null=True)),
                ("zip_code", models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("image", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("discount", models.IntegerField(blank=True, null=True)),
                (
                    "has_rebate",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                (
                    "chair_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("lounge", "Lounge Chair"),
                            ("rocking", "Rocking Chair"),
                            ("recliner", "Recliner Chair"),
                            ("accent", "Accent Chair"),
                            ("patio", "Patio Chair"),
                            ("armchair", "Armchair"),
                            ("bar_stool", "Bar Stool"),
                            ("desk", "Desk Chair"),
                            ("outdoor", "Outdoor Chair"),
                            ("chaise_lounge", "Chaise Lounge"),
                            ("folding", "Folding Chair"),
                            ("deck", "Deck Chair"),
                            ("gaming", "Gaming Chair"),
                            ("bean_bag", "Bean Bag Chair"),
                            ("dining", "Dining Chair"),
                            ("wingback", "Wingback Chair"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
            ],
        ),
    ]