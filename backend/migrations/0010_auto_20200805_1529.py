# Generated by Django 2.1.5 on 2020-08-05 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_wxdindan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wxdindan',
            name='addressid',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='地址ID'),
        ),
    ]
