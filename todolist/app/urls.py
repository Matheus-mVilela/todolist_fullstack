from django.urls import path, include
from app import views


urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("listsoftasks/", views.ListOfTaskViewSet.as_view()),
    path("listsoftasks/<int:list_task_pk>", views.ListOfTaskViewSet.as_view()),
    path("tasks/", views.TaskViewSet.as_view()),
    path("tasks/<int:task_pk>", views.TaskViewSet.as_view()),
]
