# Generated by Django 5.0.4 on 2024-05-17 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_regno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='RegNo',
        ),
    ]