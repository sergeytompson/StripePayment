# Generated by Django 4.1.7 on 2023-02-20 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stripe_payment_app", "0002_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
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
                    "percent_off",
                    models.DecimalField(
                        decimal_places=1, max_digits=3, verbose_name="Скидка"
                    ),
                ),
            ],
            options={
                "verbose_name": "Скидка",
                "verbose_name_plural": "Скидки",
            },
        ),
        migrations.CreateModel(
            name="Tax",
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
                    "display_name",
                    models.CharField(max_length=50, verbose_name="Короткое название"),
                ),
                (
                    "inclusive",
                    models.BooleanField(
                        default=False, verbose_name="Включается ли в стоимость"
                    ),
                ),
                (
                    "percentage",
                    models.DecimalField(
                        decimal_places=4, max_digits=6, verbose_name="Налоговая ставка"
                    ),
                ),
            ],
            options={
                "verbose_name": "Налог",
                "verbose_name_plural": "Налоги",
            },
        ),
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "Заказ", "verbose_name_plural": "Заказы"},
        ),
        migrations.AddField(
            model_name="order",
            name="discount",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="stripe_payment_app.discount",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="tax",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="stripe_payment_app.tax",
            ),
        ),
    ]
