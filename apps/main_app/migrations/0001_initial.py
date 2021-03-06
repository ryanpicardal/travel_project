# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('group', models.ManyToManyField(related_name='group', to='login_app.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.User')),
            ],
        ),
    ]
