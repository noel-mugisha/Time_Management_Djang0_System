# Generated by Django 5.1.2 on 2024-11-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_manager', '0003_task_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]