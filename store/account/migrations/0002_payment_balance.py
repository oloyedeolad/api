# Generated by Django 4.2 on 2023-04-07 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="balance",
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=8),
        ),
    ]
