# Generated by Django 2.1.5 on 2020-08-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20200804_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ddaddress',
            name='auser',
            field=models.CharField(max_length=5, verbose_name='用户id'),
        ),
    ]
