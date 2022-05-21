# Generated by Django 3.2.7 on 2022-05-17 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_brand_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренд'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_title',
            field=models.CharField(help_text='Mersedes', max_length=255, verbose_name='Бренд'),
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='GLS 63', max_length=255, verbose_name='Модель машины')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_brand', to='cars.brand', verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Модель машины',
                'verbose_name_plural': 'Модель машин',
            },
        ),
    ]