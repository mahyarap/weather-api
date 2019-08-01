# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-08-04 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('temperature', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestAPI.Location')),
            ],
        ),
    ]