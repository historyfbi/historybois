# Generated by Django 3.1.1 on 2020-09-15 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200913_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historypost',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='historypost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]