# Generated by Django 4.1 on 2022-08-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_alter_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="box",
            field=models.BooleanField(null=True),
        ),
    ]