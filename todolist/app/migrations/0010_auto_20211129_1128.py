# Generated by Django 3.2.9 on 2021-11-29 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211129_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listoftask',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='list_task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.listoftask'),
            preserve_default=False,
        ),
    ]
