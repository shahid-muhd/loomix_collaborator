# Generated by Django 5.0.4 on 2024-05-23 12:38

import django.utils.timezone
import payments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_subscription_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscribed_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='validity',
            field=models.DateTimeField(default=payments.models.Subscription.calculate_validity),
        ),
    ]