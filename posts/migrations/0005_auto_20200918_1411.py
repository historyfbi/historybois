# Generated by Django 3.1.1 on 2020-09-18 14:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200918_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historypost',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]