# Generated by Django 3.2.9 on 2021-12-21 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['category']},
        ),
    ]
