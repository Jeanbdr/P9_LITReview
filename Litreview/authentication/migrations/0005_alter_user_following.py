# Generated by Django 4.1.6 on 2023-02-17 10:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_rename_follows_user_following"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(
                related_name="followed_by", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
