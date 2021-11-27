from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from app import choices


class ListTaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=11, choices=choices.LIST_CHOICES, default=choices.START
    )

    @property
    def user_identification(self):
        return self.user.id

    def __srt__(self):
        return self.id, self.title


class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=11, choices=choices.TASK_CHOICES, default=choices.TO_DO
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    list_task = models.ForeignKey(ListTaskModel, on_delete=models.CASCADE, blank=False)

    @property
    def list_identification(self):
        return self.list_task.id

    def __srt__(self):
        return self.id, self.title
