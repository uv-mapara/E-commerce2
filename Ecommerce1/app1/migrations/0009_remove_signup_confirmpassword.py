# Generated by Django 4.1.7 on 2023-05-01 13:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0008_signup"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="signup",
            name="confirmpassword",
        ),
    ]
