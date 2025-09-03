from django.shortcuts import render

from .models import CaveSite, IsolationSource

# Create your views here.
def index(request): 
  return render(request, 'isolation_source/index.html', {
    'cave_sites': CaveSite.objects.all(),
    'isolation_sources': IsolationSource.objects.all()
  })