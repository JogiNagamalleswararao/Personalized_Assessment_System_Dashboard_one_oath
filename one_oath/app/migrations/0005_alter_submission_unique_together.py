# Generated by Django 4.2.1 on 2023-07-18 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_submission'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='submission',
            unique_together={('student', 'assessment')},
        ),
    ]
