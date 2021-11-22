from django.contrib.auth.models import User
from rest_framework import serializers
from app import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]


class ListTaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ListTaskModel
        fields = [
            "id",
            "user_id",
            "title",
            "start_date",
            "end_date",
            "description",
            "status",
        ]


class ListTaskCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.BooleanField()


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskModel
        fields = [
            "title",
            "start_date",
            "end_date",
            "description",
            "status",
            "list_task_id",
        ]
