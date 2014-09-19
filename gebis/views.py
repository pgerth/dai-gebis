from django.shortcuts import render_to_response, render

# Create your views here.
from django.http import HttpResponse
from gebis.models import Raeume, Mitarbeiter
 
def index(request):
    return render(request, 'gebis/index.html')
