# Generated by Django 4.1.5 on 2023-01-13 21:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('message', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completedtasks',
            old_name='task',
            new_name='tasks',
        ),
    ]
