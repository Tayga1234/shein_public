# Generated by Django 5.0.7 on 2024-08-12 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_countdown'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countdown',
            old_name='event_date',
            new_name='date',
        ),
    ]
