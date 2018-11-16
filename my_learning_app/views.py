from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.views import generic




class HomeView(generic.TemplateView):
    template_name = 'home.html'
    

