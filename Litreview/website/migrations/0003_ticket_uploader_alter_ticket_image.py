# Generated by Django 4.1.6 on 2023-02-09 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("website", "0002_alter_ticket_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="uploader",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]