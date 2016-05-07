# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20160504_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='post',
            field=models.ForeignKey(related_name='file', to='core.Post'),
        ),
        migrations.AlterField(
            model_name='image',
            name='post',
            field=models.ForeignKey(related_name='image', to='core.Post'),
        ),
    ]
