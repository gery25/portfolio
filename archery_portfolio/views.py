from django.shortcuts import render
from .models import Competitions

# Create your views here.
def home(request):
    last_competitions = Competitions.objects.all()[:3]
    return render(request, 'archery_portfolio/home.html', {'last_competitions': last_competitions})