# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name=b'Last Name')),
                ('age', models.IntegerField(verbose_name=b'Age')),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Track Name')),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='track',
            field=models.ForeignKey(to='students.Tracks'),
        ),
    ]
