from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#    return HttpResponse ('<h4>Hello python</h4>')
    return render(request, 'main/index.html')
