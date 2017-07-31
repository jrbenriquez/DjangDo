# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-31 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(max_length=255)),
                ('activeState', models.BooleanField(default=True)),
                ('doneState', models.BooleanField(default=False)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
