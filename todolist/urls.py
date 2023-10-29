from django.urls import path
from .views import TaskList, TaskCreate, TaskEdit, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>/', TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
