from django.urls import path
from .views import TaskList, TaskCreate, TaskEdit, TaskDelete, RegisterView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>/', TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
