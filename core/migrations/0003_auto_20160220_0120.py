# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160213_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='large',
            field=models.BooleanField(default=True, verbose_name=b'Large Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(verbose_name=b'Author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name=b'Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default=b'NE', max_length=2, verbose_name=b'Category', choices=[(b'NE', b'News'), (b'EV', b'Events'), (b'RU', b'Results'), (b'RO', b'Resources')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='feature',
            field=models.BooleanField(default=True, verbose_name=b'Featured'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'Title'),
        ),
    ]
