# Generated by Django 4.1 on 2022-10-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_product_box2"),
    ]

    operations = [
        migrations.CreateModel(
            name="Example",
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
                ("title", models.CharField(max_length=15)),
            ],
        ),
    ]
