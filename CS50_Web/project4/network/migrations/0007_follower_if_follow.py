# Generated by Django 5.0.4 on 2024-06-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_rename_folowers_follower_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='if_follow',
            field=models.BooleanField(default=False),
        ),
    ]
