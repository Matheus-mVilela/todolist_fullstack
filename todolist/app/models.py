from django.db import models
import datetime
from django.db.models.deletion import CASCADE
from app import choices


class SetTaskModel(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    end_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=11, choices=choices.LIST_CHOICES, default=choices.START
    )

    def __srt__(self):
        return self.id, self.title


class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    end_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=11, choices=choices.TASK_CHOICES, default=choices.TO_DO
    )
    set_task_model = models.ForeignKey(SetTaskModel, on_delete=models.CASCADE)

    def __srt__(self):
        return self.id, self.title
