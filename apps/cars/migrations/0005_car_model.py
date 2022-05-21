# Generated by Django 3.2.7 on 2022-05-17 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20220517_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='car_model', to='cars.carmodel', verbose_name='Модель'),
            preserve_default=False,
        ),
    ]
