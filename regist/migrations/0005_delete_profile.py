# Generated by Django 4.1.5 on 2023-02-11 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0004_alter_profile_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]