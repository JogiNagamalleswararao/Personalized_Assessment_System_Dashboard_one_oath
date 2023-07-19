# Generated by Django 4.2.1 on 2023-07-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uid', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(default='<django.db.models.fields.CharField>', max_length=255)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('sec', models.CharField(max_length=10)),
                ('mobile_num', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('uid', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('password', models.CharField(default='<django.db.models.fields.CharField>', max_length=255)),
                ('mobile_num', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('des', models.CharField(default='None', max_length=100)),
            ],
        ),
    ]
