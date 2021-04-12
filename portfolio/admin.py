from django.contrib import admin
from .models import Project

admin.site.site_header = 'Bad Ass Admin View'
admin.site.register(Project)
