# Generated by Django 4.1.5 on 2023-02-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlink',
            name='word',
            field=models.CharField(max_length=20, unique=True, verbose_name='Слово'),
        ),
    ]
