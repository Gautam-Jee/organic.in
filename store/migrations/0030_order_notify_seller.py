# Generated by Django 4.0.2 on 2022-05-25 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_remove_products_seller_name_products_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='notify_seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.productssellerfarmer'),
        ),
    ]