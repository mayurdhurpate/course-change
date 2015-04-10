# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(unique=True, max_length=150)),
                ('key', models.CharField(unique=True, max_length=70)),
                ('name', models.CharField(default=b'', max_length=150, null=True, blank=True)),
                ('air', models.CharField(default=b'', max_length=70, null=True, blank=True)),
                ('roll', models.CharField(default=b'', max_length=70, null=True, blank=True)),
                ('ptype', models.CharField(default=b'year4', max_length=70, null=True, blank=True)),
                ('branch', models.CharField(default=b'dummy', max_length=70, null=True, blank=True)),
                ('choice1', models.CharField(default=b'dummy', max_length=70, null=True, blank=True)),
                ('choice2', models.CharField(default=b'dummy', max_length=70, null=True, blank=True)),
                ('choice3', models.CharField(default=b'dummy', max_length=70, null=True, blank=True)),
                ('choice4', models.CharField(default=b'dummy', max_length=70, null=True, blank=True)),
                ('choice5', models.CharField(default=b'dummy', max_length=70, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
