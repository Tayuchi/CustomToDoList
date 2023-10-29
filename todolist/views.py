from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task
# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'todolist/task_list.html'
    context_object_name = 'tasks'

class TaskCreate(CreateView):
    model = Task
    template_name = 'todolist/task_create.html'
    fields = ['title']
    success_url = reverse_lazy('tasks')

class TaskEdit(UpdateView):
    model = Task
    template_name = 'todolist/task_edit.html'
    fields = ['title']
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    template_name = 'todolist/task_delete.html'
    success_url = reverse_lazy('tasks')