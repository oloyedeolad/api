# Generated by Django 4.2 on 2023-04-07 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_payment_balance"),
        ("shop", "0002_rename_requested_quantity_product_quantity_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="payment",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="account.payment",
            ),
            preserve_default=False,
        ),
    ]
