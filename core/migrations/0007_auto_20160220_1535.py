# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160220_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='post',
            name='large',
        ),
        migrations.AlterField(
            model_name='post',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name=b'Hidden'),
        ),
    ]
