# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-16 06:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('random_links', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='random_link',
            unique_together=set([('user', 'url')]),
        ),
    ]
