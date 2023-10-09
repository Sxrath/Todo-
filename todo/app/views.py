from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Tasks
from django.shortcuts import redirect

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Add_Task(LoginRequiredMixin, CreateView):
    model = Tasks
    template_name = 'task_list.html'
    fields = ['title', 'complete']     

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    success_url = reverse_lazy('tasks')

class Tasklist(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'detail.html'

    def get_queryset(self):       
        return Tasks.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['object_list']  
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

        

class Update_task(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class Delate_task(LoginRequiredMixin, DeleteView):
    model = Tasks
    success_url = reverse_lazy('tasks')

class Logout(LogoutView):
    model = Tasks
    success_url = reverse_lazy('tasks')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name = "registerpage.html"
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
