# Generated by Django 3.1.1 on 2020-09-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200918_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='historypost',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historypost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
