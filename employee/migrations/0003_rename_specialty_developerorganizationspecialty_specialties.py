# Generated by Django 4.1.5 on 2023-01-08 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developerorganizationspecialty',
            old_name='specialty',
            new_name='specialties',
        ),
    ]