# Generated by Django 3.1.2 on 2020-10-22 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmoney_info',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
