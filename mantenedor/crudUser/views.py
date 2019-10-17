from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
# importaciones
from .models import Usuario
from .forms import UsuarioForm


def index(request):
    return render(request,'paginas/index.html',{})
    
