# Generated by Django 5.0.4 on 2024-05-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_proposals_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
