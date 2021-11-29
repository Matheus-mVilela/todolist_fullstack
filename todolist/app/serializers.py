from django.contrib.auth.models import User
from rest_framework import serializers
from app import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]


class ListOfTaskDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_identification = serializers.IntegerField()
    title = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.CharField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation["tasks"] = TaskDetailSerializer(
            instance.task_set.all(), many=True
        ).data

        return representation


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.CharField()


class ListOfTaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.CharField()


class TaskDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    list_identification = serializers.IntegerField()
    title = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.CharField()


class TaskCreatelSerializer(serializers.Serializer):
    list_identification = serializers.IntegerField()
    title = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.CharField()


class TaskUpdatelSerializer(serializers.Serializer):
    title = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.CharField()
