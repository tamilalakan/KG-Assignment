# Generated by Django 3.2 on 2021-04-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_employee_viewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='viewers',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
