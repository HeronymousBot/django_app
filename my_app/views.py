from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#MTV
#M -Models
#T - Templates
#V - Views

def home(request):
    return HttpResponse('Olá, mundo!')

def home_param(request, post_id):
    return HttpResponse('Olá mundo!! %s' % post_id)