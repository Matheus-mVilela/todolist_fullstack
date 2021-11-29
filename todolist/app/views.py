from django.contrib.auth.models import Permission, User
from app import serializers, services
from rest_framework import viewsets, views, permissions, response, status
import pendulum


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListOfTaskViewSet(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, list_task_pk=None):
        if list_task_pk:
            return self._detail(list_task=list_task_pk, user=request.user.pk)

        return self._list(user=request.user.pk)

    def _detail(self, list_task, user):
        list_of_task = services.get_list_task_by_pk_and_user_id(list_task, user)
        if not list_of_task:
            return response.Response(
                {"error": "List of task not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = serializers.ListOfTaskDetailSerializer(list_of_task)

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def _list(self, user):
        lists_of_tasks = services.filter_lists_of_tasks_by_user_id(user)
        serializer = serializers.ListOfTaskDetailSerializer(lists_of_tasks, many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.ListOfTaskCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        now = pendulum.now().strftime("%Y-%m-%dT%H:%M:%S")
        user = request.user
        title = serializer.data["title"]
        start_date = serializer.data["start_date"]
        end_date = serializer.data["end_date"]
        description = serializer.data["description"]
        c_status = serializer.data["status"]

        if start_date < now:
            return response.Response(
                {"error": "Start date less than now!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if start_date >= end_date:
            return response.Response(
                {"error": "End date less than or equal to startdate!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        list_task = services.chek_equal_list_task(user, title, description)

        if not list_task:
            return response.Response(
                {"error": "Task duplicate, title or description equal a task exist!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        list_of_task = services.create_list_of_task(
            user, title, start_date, end_date, description, c_status
        )

        if not list_of_task:
            return response.Response(
                {"error": "Error at created!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = serializers.ListOfTaskDetailSerializer(list_of_task)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, list_task_pk):
        serializer = serializers.ListOfTaskCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        list_of_task = services.get_list_task_by_pk_and_user_id(
            list_task_pk, user=request.user
        )
        if not list_of_task:
            return response.Response(
                {"error": "List of task not found!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        now = pendulum.now().strftime("%Y-%m-%dT%H:%M:%S")
        title = serializer.data["title"]
        start_date = serializer.data["start_date"]
        end_date = serializer.data["end_date"]
        description = serializer.data["description"]
        c_status = serializer.data["status"]

        if start_date < now:
            return response.Response(
                {"error": "Start date less than now!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if start_date >= end_date:
            return response.Response(
                {"error": "End date less than or equal to startdate!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        list_task = services.chek_equal_list_task(request.user, title, description)

        if not list_task:
            return response.Response(
                {"error": "Task duplicate, title or description equal a task exist!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        update_list_of_task = services.update_list_of_task(
            list_of_task, title, start_date, end_date, description, c_status
        )

        if not update_list_of_task:
            return response.Response(
                {"error": "Error at update!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = serializers.ListOfTaskDetailSerializer(update_list_of_task)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, list_task_pk):
        list_of_task = services.get_list_task_by_pk_and_user_id(
            list_task_pk, user=request.user
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


class TaskViewSet(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, task_pk=None):
        if task_pk:
            return self._detail(task_pk=task_pk, user=request.user.pk)

        return self._list(user=request.user.pk)

    def _detail(self, task_pk, user):
        task = services.get_task_by_pk_and_user_id(task_pk, user)

        if not task:
            return response.Response(
                {"error": "Task not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = serializers.TaskDetailSerializer(task)

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def _list(self, user):

        tasks = services.filter_tasks_by_user_id(user)
        serializer = serializers.TaskDetailSerializer(tasks, many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.TaskCreatelSerializer(data=request.data)

        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        now = pendulum.now().strftime("%Y-%m-%dT%H:%M:%S")
        user = request.user
        list_identification = serializer["list_identification"].value
        title = serializer.data["title"]
        start_date = serializer.data["start_date"]
        end_date = serializer.data["end_date"]
        description = serializer.data["description"]
        c_status = serializer.data["status"]

        list_identification = services.check_list_of_task(list_identification, user)

        if start_date < now:
            return response.Response(
                {"error": "Start date less than now!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if start_date >= end_date:
            return response.Response(
                {"error": "End date less than or equal to startdate!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        task = services.chek_equal_task(list_identification, title, description)

        if not task:
            return response.Response(
                {"error": "Task duplicate, title or description equal a task exist!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        task = services.create_task(
            user,
            list_identification,
            title,
            start_date,
            end_date,
            description,
            c_status,
        )
        if not task:
            return response.Response(
                {"error": "Error at created!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = serializers.TaskDetailSerializer(task)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, task_pk):
        serializer = serializers.TaskUpdatelSerializer(data=request.data)

        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        task = services.get_task_by_pk_and_user_id(task_pk, user=request.user)

        if not task:
            return response.Response(
                {"error": "Task not found!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        now = pendulum.now().strftime("%Y-%m-%dT%H:%M:%S")
        title = serializer.data["title"]
        start_date = serializer.data["start_date"]
        end_date = serializer.data["end_date"]
        description = serializer.data["description"]
        c_status = serializer.data["status"]

        if start_date < now:
            return response.Response(
                {"error": "Start date less than now!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if start_date >= end_date:
            return response.Response(
                {"error": "End date less than or equal to startdate!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        update_task = services.update_task(
            task, title, start_date, end_date, description, c_status
        )

        if not update_task:
            return response.Response(
                {"error": "Error at update!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = serializers.TaskDetailSerializer(update_task)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, task_pk):
        task = services.get_task_by_pk_and_user_id(task_pk, user=request.user)

        if not task:
            return response.Response(
                {"error": "Task not found!"},
                status=status.HTTP_404_NOT_FOUND,
            )

        task.delete()

        return response.Response(
            {"messege": "Sucess, deleted!"}, status=status.HTTP_204_NO_CONTENT
        )
