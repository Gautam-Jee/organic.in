# Generated by Django 4.0.2 on 2022-05-18 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_rename_customer_productssellerfarmer_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date']},
        ),
    ]