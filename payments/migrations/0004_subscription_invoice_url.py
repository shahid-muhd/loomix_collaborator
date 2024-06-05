# Generated by Django 5.0.4 on 2024-05-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_subscription_projects_left'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='invoice_url',
            field=models.URLField(default='http://localhost:8000/', help_text='Invoice URL'),
            preserve_default=False,
        ),
    ]