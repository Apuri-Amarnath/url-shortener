# Generated by Django 5.0.3 on 2024-04-01 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=225, unique=True)),
                ('short_url', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
