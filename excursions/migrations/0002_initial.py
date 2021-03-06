# Generated by Django 3.2.4 on 2021-06-10 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('excursions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='guide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excursions', to=settings.AUTH_USER_MODEL, verbose_name='Гид'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='tags',
            field=models.ManyToManyField(blank=True, to='excursions.Tag', verbose_name='Теги'),
        ),
    ]
