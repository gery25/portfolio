from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    top_projects = Project.objects.all()[:3]
    return render(request, 'developer_portfolio/home.html', {'top_projects': top_projects})
