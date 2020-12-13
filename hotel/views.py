from django.shortcuts import render
from .models import suits

# Create your views here.

def index(request):
    return render(request,'index.html')

def rooms(request):

    rtypes = suits.objects.all()
    return render(request,'rooms.html', {'rtypes' : rtypes})
