# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-09 11:20
from __future__ import unicode_literals

import django.contrib.sites.managers
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('users', '0003_auto_20160329_2003'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='site',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sites.Site'),
        ),
    ]
