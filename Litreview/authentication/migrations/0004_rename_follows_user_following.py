# Generated by Django 4.1.6 on 2023-02-16 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_user_follows"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="follows",
            new_name="following",
        ),
    ]
