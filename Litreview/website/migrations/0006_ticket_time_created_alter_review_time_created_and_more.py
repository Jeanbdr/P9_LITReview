# Generated by Django 4.1.6 on 2023-02-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_alter_ticket_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="time_created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="review",
            name="time_created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="description",
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]