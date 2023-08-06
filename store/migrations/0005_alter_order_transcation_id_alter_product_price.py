# Generated by Django 4.2.1 on 2023-08-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_alter_order_complete_alter_orderitem_order_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="transcation_id",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
