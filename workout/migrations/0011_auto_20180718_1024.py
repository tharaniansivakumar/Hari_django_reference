# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0010_auto_20180718_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='manychild',
            fields=[
                ('child_id', models.IntegerField(serialize=False, primary_key=True)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='manyparent',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='manychild',
            name='info',
            field=models.ForeignKey(to='workout.manyparent'),
        ),
    ]
