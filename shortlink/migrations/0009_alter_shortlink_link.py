# Generated by Django 4.1.5 on 2023-02-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlink', '0008_alter_shortlink_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlink',
            name='link',
            field=models.URLField(max_length=250, verbose_name='Ссылка'),
        ),
    ]
