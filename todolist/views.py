from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task
# Create your views here.

class RegisterPage(FormView):
    template_name = 'todolist/auth_register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'todolist/auth_login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(ListView, LoginRequiredMixin):
    model = Task
    template_name = 'todolist/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user)
        else:
            return Task.objects.none()

class TaskCreate(CreateView, LoginRequiredMixin):
    model = Task
    template_name = 'todolist/task_create.html'
    fields = ['title']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskEdit(UpdateView, LoginRequiredMixin):
    model = Task
    template_name = 'todolist/task_edit.html'
    fields = ['title']
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView, LoginRequiredMixin):
    model = Task
    template_name = 'todolist/task_delete.html'
    success_url = reverse_lazy('tasks')