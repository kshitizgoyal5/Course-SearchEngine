# Generated by Django 3.2.9 on 2021-12-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_auto_20211208_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.TextField(default=''),
        ),
    ]