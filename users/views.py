from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import User


class IndexView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        return User.objects.all()


class CreateUser(generic.CreateView):
    model = User
    fields = ['Name', 'Phone_no']
    template_name = 'users/add.html'
    success_url = reverse_lazy('users:index')


class UpdateUser(generic.UpdateView):
    model = User
    fields = ['Name', 'Phone_no']
    template_name = 'users/add.html'
    success_url = reverse_lazy('users:index')


class DeleteUser(generic.DeleteView):
    model = User
    success_url = reverse_lazy('users:index')