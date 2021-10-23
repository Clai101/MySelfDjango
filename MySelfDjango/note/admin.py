from django.contrib import admin
from note.models import *
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('orign', 'title', "another_information")
    search_fields = ('title','another_information', 'orign')

admin.site.register(News, NewsAdmin)