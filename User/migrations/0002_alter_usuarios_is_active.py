# Generated by Django 4.1.2 on 2023-01-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
