from django.urls import path, include
from app import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("listsoftasks/", views.ListOfTaskViewSet.as_view()),
    path("listsoftasks/<int:list_task_pk>", views.ListOfTaskViewSet.as_view()),
    path("tasks/", views.TaskViewSet.as_view()),
    path("tasks/<int:task_pk>", views.TaskViewSet.as_view()),
]
