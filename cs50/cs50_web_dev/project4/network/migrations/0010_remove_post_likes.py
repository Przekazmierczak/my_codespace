# Generated by Django 4.2.3 on 2023-08-21 18:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0009_alter_likes_post"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="likes",
        ),
    ]
