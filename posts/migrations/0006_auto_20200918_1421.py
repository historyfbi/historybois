# Generated by Django 3.1.1 on 2020-09-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200918_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historypost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='historypost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
