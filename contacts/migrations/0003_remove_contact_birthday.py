# Generated by Django 3.1.4 on 2021-01-10 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20210108_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='birthday',
        ),
    ]
