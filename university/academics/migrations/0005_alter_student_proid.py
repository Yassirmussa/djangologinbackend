# Generated by Django 5.0 on 2023-12-30 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_studentcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ProID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='academics.program'),
        ),
    ]