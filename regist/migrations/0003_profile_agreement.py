# Generated by Django 4.1.5 on 2023-02-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0002_alter_profile_options_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='agreement',
            field=models.BooleanField(default=True, verbose_name='Пользовательское соглашение'),
        ),
    ]