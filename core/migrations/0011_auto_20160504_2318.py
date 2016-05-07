# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_post_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'Title')),
                ('description', models.CharField(max_length=128, verbose_name=b'Description')),
                ('file', models.FileField(upload_to=b'files/%Y/%m')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'Title')),
                ('description', models.CharField(max_length=128, verbose_name=b'Description')),
                ('image', models.ImageField(upload_to=b'images/%Y/%m')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(to='core.Post'),
        ),
        migrations.AddField(
            model_name='file',
            name='post',
            field=models.ForeignKey(to='core.Post'),
        ),
    ]
