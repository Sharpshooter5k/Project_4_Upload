# Generated by Django 3.2.9 on 2021-12-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_todo_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='updated',
            field=models.BooleanField(default=False),
        ),
    ]
