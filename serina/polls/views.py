from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(resquest):
    return render(resquest, 'serina_views/index.html')
