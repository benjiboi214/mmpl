# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name=b'Hide Post'),
        ),
    ]
