# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0010_auto_20171231_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='img',
            field=models.ImageField(blank=True, default='img/def.jpg', upload_to='img/', verbose_name='Афиша'),
        ),
    ]
