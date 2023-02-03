# Generated by Django 4.1.5 on 2023-01-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[
                    ("Sales Contact", "Sales Contact"),
                    ("Support Contact", "Support Contact"),
                ],
                max_length=50,
                null=True,
                verbose_name="Role",
            ),
        ),
    ]
