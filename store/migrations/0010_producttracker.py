# Generated by Django 4.0.2 on 2022-05-13 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productStatus', models.CharField(choices=[('1', 'Ordered'), ('2', 'On the way'), ('3', 'Delivered'), ('4', 'Refused')], default='1', max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
        ),
    ]
