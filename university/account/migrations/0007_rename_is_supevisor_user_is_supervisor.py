# Generated by Django 5.0.6 on 2024-05-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_is_pgo_user_is_examiner_user_is_supevisor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_supevisor',
            new_name='is_supervisor',
        ),
    ]
