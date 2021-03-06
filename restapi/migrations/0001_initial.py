# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2017-09-05 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'apartment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'discipline',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DisciplineType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'discipline_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
                ('balance', models.FloatField()),
                ('gender', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'dormitory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'manage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MoveDormitory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'move_dormitory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sanitation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('score', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'sanitation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('paid', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('reside_date', models.DateField()),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
    ]
