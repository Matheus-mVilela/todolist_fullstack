# Generated by Django 3.2.9 on 2021-11-19 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20211116_0918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskmodel',
            old_name='list_task_model',
            new_name='list_task_id',
        ),
        migrations.AddField(
            model_name='listtaskmodel',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
