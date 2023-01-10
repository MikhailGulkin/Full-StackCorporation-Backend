# Generated by Django 4.1.5 on 2023-01-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('employee', '0007_alter_developer_team'),
        ('project', '0008_alter_team_project_manager_alter_team_team_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='developers',
            field=models.ManyToManyField(blank=True, null=True,
                                         related_name='developers',
                                         to='employee.developer'),
        ),
    ]
