# Generated by Django 4.1.6 on 2023-02-10 16:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_user_email_alter_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="follows",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
