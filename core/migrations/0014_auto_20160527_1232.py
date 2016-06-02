# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_post_image_primary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_primary',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(default=b'LG', max_length=2, verbose_name=b'Post Type', choices=[(b'LG', b'Large'), (b'SM', b'Small'), (b'FE', b'Feature'), (b'IM', b'Image')]),
        ),
    ]
