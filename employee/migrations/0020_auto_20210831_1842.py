# Generated by Django 3.2.6 on 2021-08-31 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_auto_20210831_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_shift',
            name='closing_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='office_shift',
            name='starting_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
