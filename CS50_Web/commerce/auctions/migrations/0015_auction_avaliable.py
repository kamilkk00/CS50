# Generated by Django 5.0.4 on 2024-05-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='avaliable',
            field=models.BooleanField(default=True),
        ),
    ]
