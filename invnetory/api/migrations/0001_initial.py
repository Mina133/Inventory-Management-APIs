# Generated by Django 5.1.4 on 2025-01-11 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Quantity', models.IntegerField()),
                ('Price', models.FloatField()),
                ('Date_Added', models.DateField(auto_now_add=True)),
                ('Last_Update', models.DateField(auto_now=True)),
                ('low_stock_threshold', models.PositiveIntegerField(default=10)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categories')),
            ],
        ),
    ]
