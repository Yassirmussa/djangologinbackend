# Generated by Django 5.0.4 on 2024-05-01 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='ProID',
        ),
        migrations.RemoveField(
            model_name='studentcourse',
            name='CoID',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ProID',
        ),
        migrations.RemoveField(
            model_name='student',
            name='UserID',
        ),
        migrations.RemoveField(
            model_name='studentcourse',
            name='StuID',
        ),
        migrations.DeleteModel(
            name='Todos',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentCourse',
        ),
    ]