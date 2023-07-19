# Generated by Django 4.2.1 on 2023-07-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('uid', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('student', models.BooleanField(default=False)),
                ('teacher', models.BooleanField(default=False)),
            ],
        ),
    ]
