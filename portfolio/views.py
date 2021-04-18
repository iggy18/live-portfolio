from django.shortcuts import render
from .models import Project
from django.views.generic import DetailView
from django.conf import settings

def portfolio(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'portfolio/home.html', context)

class DetailView(DetailView):
    template_name = 'portfolio/detail.html'
    model = Project

def error_404_view(request, exception):
    return render(request, 'portfolio/404.html')