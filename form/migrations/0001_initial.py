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
                ('name', models.CharField(max_length=150, null=True, blank=True)),
                ('air', models.CharField(max_length=70, null=True, blank=True)),
                ('roll', models.CharField(max_length=70, null=True, blank=True)),
                ('ptype', models.CharField(max_length=70, null=True, blank=True)),
                ('branch', models.CharField(max_length=70, null=True, blank=True)),
                ('choice1', models.CharField(max_length=70, null=True, blank=True)),
                ('choice2', models.CharField(max_length=70, null=True, blank=True)),
                ('choice3', models.CharField(max_length=70, null=True, blank=True)),
                ('choice4', models.CharField(max_length=70, null=True, blank=True)),
                ('choice5', models.CharField(max_length=70, null=True, blank=True)),
                ('spi1', models.CharField(max_length=70, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
