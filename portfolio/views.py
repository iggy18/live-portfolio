from django.shortcuts import render
from .models import Project
from django.views.generic import DetailView

def portfolio(request):
    return render(request, 'portfolio/home.html')

class DetailView(DetailView):
    template_name = 'portfolio/detail.html'
    model = Project
