# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160220_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default=b'LG', max_length=2, verbose_name=b'Post Type', choices=[(b'LG', b'Large'), (b'SM', b'Small'), (b'FE', b'Feature')]),
        ),
    ]
