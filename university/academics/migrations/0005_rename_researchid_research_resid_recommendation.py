# Generated by Django 5.0.4 on 2024-05-18 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='research',
            old_name='ResearchID',
            new_name='ResID',
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('RecID', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=250)),
                ('ResID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.research')),
            ],
            options={
                'db_table': 'recommendation',
            },
        ),
    ]