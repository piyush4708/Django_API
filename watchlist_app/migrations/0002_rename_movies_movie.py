# Generated by Django 5.2 on 2025-04-28 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Movies",
            new_name="Movie",
        ),
    ]
