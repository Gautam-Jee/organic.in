# Generated by Django 4.0.2 on 2022-05-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_alter_products_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='description',
        ),
        migrations.AddField(
            model_name='products',
            name='seller_name',
            field=models.CharField(default='official team', max_length=200),
        ),
    ]
