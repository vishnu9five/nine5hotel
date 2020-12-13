from django.shortcuts import render
from .models import suits

# Create your views here.

def index(request):
    return render(request,'index.html')

def rooms(request):

    rtype1 = suits()
    rtype1.name ='luxury suit'
    rtype1.desc ='It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,'
    rtype1.price ='800'
    rtype1.offer=False

    rtype2 = suits()
    rtype2.name ='eco suit'
    rtype2.desc ='It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,'
    rtype2.price ='200'
    rtype1.offer=True
    
    rtypes = [rtype1,rtype2]

    return render(request,'rooms.html', {'rtypes' : rtypes})
