from django.contrib.auth.models import User
from rest_framework import serializers
from app import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]


class ListTaskDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_identification = serializers.IntegerField()
    title = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.CharField()


class ListTaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.CharField()


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
