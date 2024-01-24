# Generated by Django 4.2.9 on 2024-01-22 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "name",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemModel",
            fields=[
                (
                    "name",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("depreciation_percent", models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name="InventoryModel",
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
                ("quantity", models.IntegerField(default=0)),
                ("price", models.FloatField(help_text="Price of each commodity.")),
                ("current_price", models.FloatField()),
                (
                    "buy_date",
                    models.DateField(help_text="Enter Date in YYYY-MM-DD format."),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.itemmodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CommodityModel",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("assign_to", models.CharField(blank=True, max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Functional", "Functional"),
                            ("Non-functional", "Non-functional"),
                        ],
                        default="Functional",
                        max_length=20,
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.department",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.itemmodel",
                    ),
                ),
            ],
        ),
    ]
