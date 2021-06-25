# Generated by Django 3.2.4 on 2021-06-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='price_child',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Стоимость для детей'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='price_group',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Стоимость для группы'),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Стоимость для взрослых'),
        ),
    ]
