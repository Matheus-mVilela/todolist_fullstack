from django.contrib.auth.models import User
from app import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, views, permissions, response, status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListTaskViewSet(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, list_task_pk=None):
        if list_task_pk:
            return self._detail(list_task_pk=list_task_pk, user_id=request.user.pk)

        return self._list(user_id=request.user.pk)

    def _detail(self, list_task_pk, user_id):
        list_of_task = models.ListTaskModel.objects.filter(
            pk=list_task_pk, user_id=user_id
        )

        if not list_of_task:
            return response.Response(
                {"error": "List of task not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = serializers.ListTaskDetailSerializer(list_of_task)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def _list(self, user_id):

        lists_of_tasks = models.ListTaskModel.objects.filter(user_id=user_id)

        serializer = serializers.ListTaskDetailSerializer(lists_of_tasks, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.ListTaskDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            list_of_task = models.ListTaskModel.objects.create(
                user_id=request.user,
                title=serializer.data["title"],
                start_date=serializer.data["start_date"],
                end_date=serializer.data["end_date"],
                description=serializer.data["description"],
                status=serializer.data["status"],
            )

        except ValueError as error:
            return response.Response(
                {"error": str(error)}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = serializers.ListTaskCreateSerializer(list_of_task)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def put():
        pass

    def patch():
        pass

    def delete():
        pass


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.TaskModel.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["list_task_id"]
