from django.urls import path, include
from rest_framework import routers
from app import views


app_name = "app"

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskViewSet, basename="tasks")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("listsoftasks/", views.ListTaskViewSet.as_view()),
    path("listsoftasks/<int:list_task_pk>", views.ListTaskViewSet.as_view()),
]
