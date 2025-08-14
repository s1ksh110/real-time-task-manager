from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # Auto-creates CRUD URLs like /tasks/, /tasks/{id}/.

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]