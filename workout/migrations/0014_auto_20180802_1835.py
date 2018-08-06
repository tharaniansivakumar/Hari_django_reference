# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0013_csvdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manyparent',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'parent_name'),
        ),
    ]
