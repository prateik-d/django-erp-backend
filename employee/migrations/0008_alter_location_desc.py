# Generated by Django 3.2.6 on 2021-08-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_alter_location_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
