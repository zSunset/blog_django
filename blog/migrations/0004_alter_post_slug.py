# Generated by Django 4.2 on 2023-04-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_delete_publishedmanager"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
    ]
