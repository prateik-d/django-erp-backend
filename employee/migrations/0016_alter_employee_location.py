# Generated by Django 3.2.6 on 2021-08-31 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_auto_20210831_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='employee.location'),
        ),
    ]
