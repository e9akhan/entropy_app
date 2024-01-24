# Generated by Django 4.2.9 on 2024-01-22 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0003_remove_commoditymodel_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="commoditymodel",
            name="item",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="inventory.itemmodel",
            ),
            preserve_default=False,
        ),
    ]