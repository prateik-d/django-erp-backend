# Generated by Django 3.2.6 on 2021-08-31 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_auto_20210831_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]