# Generated by Django 3.1.1 on 2020-09-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20200915_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='historypost',
            name='updated',
            field=models.BooleanField(default=False),
        ),
    ]