# Generated by Django 5.0.6 on 2024-06-13 12:01

import django.db.models.deletion
import django.utils.timezone
import uuid
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
                (
                    "name",
                    models.CharField(
                        help_text="name of order", max_length=300, verbose_name="name"
                    ),
                ),
                ("quantity", models.IntegerField(help_text="quantity in order")),
                ("price", models.DecimalField(decimal_places=2, max_digits=200)),
                ("weigth", models.DecimalField(decimal_places=2, max_digits=200)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Shipping",
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
                ("id_inteface", models.UUIDField(default=uuid.uuid4)),
                ("address", models.CharField(max_length=300)),
                ("owner_name", models.CharField(max_length=300)),
                ("owner_email", models.EmailField(max_length=300)),
                (
                    "shipment_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "pendin"), ("shipping", "shipped")],
                        default="pending",
                        max_length=200,
                    ),
                ),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="order.order"
                    ),
                ),
            ],
        ),
    ]