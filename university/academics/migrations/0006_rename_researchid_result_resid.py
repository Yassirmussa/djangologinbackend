# Generated by Django 5.0.6 on 2024-05-18 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_rename_researchid_research_resid_recommendation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='ResearchID',
            new_name='ResID',
        ),
    ]
