# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import weblate.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0008_auto_20181015_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('details', weblate.utils.fields.JSONField(default={})),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Component')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='change',
            name='action',
            field=models.IntegerField(choices=[(0, 'Resource update'), (1, 'Translation completed'), (2, 'Translation changed'), (5, 'New translation'), (3, 'Comment added'), (4, 'Suggestion added'), (6, 'Automatic translation'), (7, 'Suggestion accepted'), (8, 'Translation reverted'), (9, 'Translation uploaded'), (10, 'Glossary added'), (11, 'Glossary updated'), (12, 'Glossary uploaded'), (13, 'New source string'), (14, 'Component locked'), (15, 'Component unlocked'), (16, 'Detected duplicate string'), (17, 'Committed changes'), (18, 'Pushed changes'), (19, 'Reset repository'), (20, 'Merged repository'), (21, 'Rebased repository'), (22, 'Failed merge on repository'), (23, 'Failed rebase on repository'), (28, 'Failed push on repository'), (24, 'Parse error'), (25, 'Removed translation'), (26, 'Suggestion removed'), (27, 'Search and replace'), (29, 'Suggestion removed during cleanup'), (30, 'Source string changed'), (31, 'New string added'), (32, 'Mass state change'), (33, 'Changed visibility'), (34, 'Added user'), (35, 'Removed user'), (36, 'Translation approved'), (37, 'Marked for edit'), (38, 'Removed component'), (39, 'Removed project'), (40, 'Duplicate language found')], default=2),
        ),
        migrations.AlterUniqueTogether(
            name='alert',
            unique_together=set([('component', 'name')]),
        ),
    ]