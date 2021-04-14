from django.shortcuts import render
from .models import Project
from django.views.generic import DetailView

def portfolio(request):
    projects = Project.objects.all()[::-1]
    context = {"projects": projects}
    return render(request, 'portfolio/home.html', context)

class DetailView(DetailView):
    template_name = 'portfolio/detail.html'
    model = Project
