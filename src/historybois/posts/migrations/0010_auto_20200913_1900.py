# Generated by Django 3.1.1 on 2020-09-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200913_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historypost',
            name='uid',
            field=models.CharField(editable=False, max_length=4, primary_key=True, serialize=False, unique=True),
        ),
    ]
