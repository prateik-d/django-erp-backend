# Generated by Django 3.2.6 on 2021-08-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_created=True)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
    ]