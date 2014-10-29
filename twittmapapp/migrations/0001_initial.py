# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweetdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_str', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('longitude', models.DecimalField(max_digits=16, decimal_places=8)),
                ('latitude', models.DecimalField(max_digits=16, decimal_places=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
