# Generated by Django 4.1.7 on 2023-02-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_payment_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='stripe_payment_app.item')),
            ],
        ),
    ]
