# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twittmapapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='tweetdata',
            name='id_str',
            field=models.CharField(max_length=40, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
