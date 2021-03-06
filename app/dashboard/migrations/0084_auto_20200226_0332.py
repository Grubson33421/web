# Generated by Django 2.2.4 on 2020-02-26 03:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0083_auto_20200215_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='cached_view_props',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='activity',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
