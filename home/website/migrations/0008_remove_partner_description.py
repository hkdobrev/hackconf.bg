# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-07 07:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_partner_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='description',
        ),
    ]