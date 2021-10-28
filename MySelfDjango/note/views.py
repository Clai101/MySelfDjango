from django.shortcuts import render
from django.views.generic import DetailView
from django.views import View
from note.templates.it_news import *
from note.templates.space_news import *
from note.templates.bin_sort import *
# Create your views here.

class MainListView(View):
    def get(self, request, *args, **kwargs):
        last_news = it_get_in_json() + get_in_json()
        last_news = heap_sort(last_news)
        context = {'last_news':last_news}
        print(context["last_news"])
        return render(request, 'note/WebPage1_pattern.html', context)