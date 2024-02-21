# Generated by Django 4.2 on 2024-02-19 10:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemRate",
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
                ("item_name", models.CharField(max_length=100)),
                ("rate", models.TextField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("image_url", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OrderItems",
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
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "item_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.itemrate",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "image_proof",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("total_amount", models.IntegerField(default=0)),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("live", "Live"),
                            ("onhold", "On Hold"),
                            ("completed", "Completed"),
                            ("rejected", "Rejected"),
                            ("picked", "Picked"),
                            ("paid", "Paid"),
                        ],
                        default="onhold",
                        max_length=100,
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        through="orders.OrderItems", to="orders.itemrate"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PickupRequest",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("pickup_date", models.DateField()),
                ("pickup_time", models.TimeField()),
                ("flat_number", models.TextField()),
                ("area", models.TextField()),
                ("landmark", models.TextField(blank=True, null=True)),
                ("city", models.TextField()),
                ("state", models.TextField()),
                ("pincode", models.CharField(max_length=6)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("requested", "Requested"),
                            ("completed", "Completed"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="requested",
                        max_length=100,
                    ),
                ),
                ("contact_person_name", models.CharField(max_length=255)),
                (
                    "contact_person_number",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be 10 digits only.",
                                regex="^\\d{10}",
                            )
                        ],
                    ),
                ),
                (
                    "address_type",
                    models.CharField(
                        choices=[("office", "Office"), ("home", "Home")],
                        default="office",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserTransactionDetails",
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
                ("transactionId", models.TextField()),
                ("total_amount", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.orders",
                    ),
                ),
                (
                    "userId",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PickupRequestItem",
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
                ("weight", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "item_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.itemrate",
                    ),
                ),
                (
                    "pickup_request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.pickuprequest",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pickuprequest",
            name="items",
            field=models.ManyToManyField(
                through="orders.PickupRequestItem", to="orders.itemrate"
            ),
        ),
        migrations.AddField(
            model_name="pickuprequest",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="pickup_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pickup_id",
                to="orders.pickuprequest",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="vendor_id",
            field=models.ForeignKey(
                limit_choices_to={"is_vendor": True},
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="orderitems",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.orders",
            ),
        ),
        migrations.CreateModel(
            name="MyCartItems",
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
                ("weight", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "item_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.itemrate",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("user", "item_id")},},
        ),
    ]