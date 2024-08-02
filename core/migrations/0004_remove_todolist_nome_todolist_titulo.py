# Generated by Django 5.0.7 on 2024-08-02 01:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_todolist_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='nome',
        ),
        migrations.AddField(
            model_name='todolist',
            name='titulo',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Titulo'),
            preserve_default=False,
        ),
    ]