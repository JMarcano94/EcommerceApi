# Generated by Django 4.1.2 on 2023-01-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('section', models.CharField(default=None, max_length=20)),
                ('description', models.CharField(default=None, max_length=100)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio Unitario')),
            ],
        ),
    ]
