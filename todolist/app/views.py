from django.contrib.auth.models import User
from app import models, serializers, services
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, views, permissions, response, status
import pendulum


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
        list_of_task = services.get_list_task_by_pk_and_user_id(
            list_task_pk=list_task_pk, user_id=user_id
        )
        if not list_of_task:
            return response.Response(
                {"error": "List of task not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = serializers.ListTaskDetailSerializer(list_of_task)

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def _list(self, user_id):
        lists_of_tasks = services.filter_lists_of_tasks_by_user_id(user_id=user_id)
        serializer = serializers.ListTaskDetailSerializer(lists_of_tasks, many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.ListTaskCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        _now = pendulum.now().strftime("%Y-%m-%dT%H:%M:%S")
        _user_id = request.user
        _title = serializer.data["title"]
        _start_date = serializer.data["start_date"]
        _end_date = serializer.data["end_date"]
        _description = serializer.data["description"]
        _status = serializer.data["status"]

        if _start_date < _now:
            return response.Response(
                {"error": "Start date less than now!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if _start_date >= _end_date:
            return response.Response(
                {"error": "End date less than or equal to startdate!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        list_of_task = services.create_list_of_task(
            _user_id, _title, _start_date, _end_date, _description, _status
        )

        if not list_of_task:
            return response.Response(
                {"error": "Error at created!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = serializers.ListTaskDetailSerializer(list_of_task)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, list_task_pk):
        serializer = serializers.ListTaskCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        list_of_task = services.get_list_task_by_pk_and_user_id(
            list_task_pk=list_task_pk, user_id=request.user
        )
        if not list_of_task:
            return response.Response(
                {"error": "List of task not found!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        _now = pendulum.now().strftime("%Y-%m-%dT%H:%M:%S")
        _title = serializer.data["title"]
        _start_date = serializer.data["start_date"]
        _end_date = serializer.data["end_date"]
        _description = serializer.data["description"]
        _status = serializer.data["status"]

        if _start_date < _now:
            return response.Response(
                {"error": "Start date less than now!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if _start_date >= _end_date:
            return response.Response(
                {"error": "End date less than or equal to startdate!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        update_list_of_task = services.update_list_of_task(
            list_of_task, _title, _start_date, _end_date, _description, _status
        )

        if not update_list_of_task:
            return response.Response(
                {"error": "Error at update!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = serializers.ListTaskDetailSerializer(update_list_of_task)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, list_task_pk):
        list_of_task = services.get_list_task_by_pk_and_user_id(
            list_task_pk=list_task_pk, user_id=request.user
        )
        if not list_of_task:
            return response.Response(
                {"error": "List of task not found!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        list_of_task.delete()

        return response.Response(
            {"messege": "Sucess, deleted!"}, status=status.HTTP_204_NO_CONTENT
        )


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.TaskModel.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["list_task_id"]
