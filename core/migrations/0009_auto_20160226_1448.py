# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to=b'files/%Y/%m', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=b'images/%Y/%m', blank=True),
        ),
    ]
