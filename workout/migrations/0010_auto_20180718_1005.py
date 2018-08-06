# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0009_autoid'),
    ]

    operations = [
        migrations.CreateModel(
            name='child',
            fields=[
                ('child_id', models.IntegerField(serialize=False, primary_key=True)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='parent',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='info',
            field=models.OneToOneField(to='workout.parent'),
        ),
    ]
