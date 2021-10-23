from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from .models import *

# Create your views here.

class News_list(ListView):
    model = News
    context_object_name = 'table'
    template_name = 'app/mainpage.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Агрекатор новостей'
        context['menu'] = menu
        return context
    def get_queryset(self):
        return App.objects.all(is_published=True)