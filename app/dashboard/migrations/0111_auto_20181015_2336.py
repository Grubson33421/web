# Generated by Django 2.1.1 on 2018-10-15 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0110_auto_20181027_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='tokenAddress',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
