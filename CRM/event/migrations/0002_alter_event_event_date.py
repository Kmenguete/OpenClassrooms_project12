# Generated by Django 4.1.5 on 2023-01-31 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event_date",
            field=models.DateTimeField(),
        ),
    ]
