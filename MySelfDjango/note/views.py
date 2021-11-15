from django.shortcuts import render
from django.views import View
from note.pars_defs.it_news import *
from note.pars_defs.space_news import *
from note.pars_defs.bin_sort import *

class MainListView(View):
    def get(self, request, *args, **kwargs):
        last_news = it_get_in_json() + get_in_json()
        print(it_get_in_json())
        last_news = heap_sort(last_news)
        context = {'last_news':last_news,}
        return render(request, 'note/main_news.html', context)