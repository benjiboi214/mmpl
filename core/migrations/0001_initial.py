# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 2, 13, 6, 6, 51, 11682, tzinfo=utc))),
                ('category', models.CharField(default=b'NE', max_length=2, choices=[(b'NE', b'News'), (b'EV', b'Events'), (b'RU', b'Results'), (b'RO', b'Resources')])),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('feature', models.BooleanField(default=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
