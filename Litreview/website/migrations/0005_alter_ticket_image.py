# Generated by Django 4.1.6 on 2023-02-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0004_alter_ticket_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]