# Generated by Django 4.1.5 on 2023-01-10 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('project', '0008_alter_team_project_manager_alter_team_team_lead'),
        ('employee', '0005_alter_developer_team_alter_projectmanager_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='team',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='developer_team',
                                    to='project.team'),
        ),
    ]
