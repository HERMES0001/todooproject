# Generated by Django 4.2.4 on 2023-09-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date",
            field=models.DateField(default="2000-03-23"),
            preserve_default=False,
        ),
    ]
