# Generated by Django 5.0.4 on 2024-05-01 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_remove_course_proid_remove_studentcourse_coid_and_more'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
