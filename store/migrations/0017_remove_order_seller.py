# Generated by Django 4.0.2 on 2022-05-16 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_order_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='seller',
        ),
    ]