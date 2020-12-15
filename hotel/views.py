from django.shortcuts import render
from .models import suits

# Create your views here.

def index(request):
    return render(request,'index.html')

def rooms(request):

    rtypes = suits.objects.all()
    return render(request,'rooms.html', {'rtypes' : rtypes})

def product(request):
    if request.method=='GET':
        sku = request.GET.get('sku')
        if not sku:
            return render(request,'rooms.html')
        else:
            # now you have the value of sku
            # so you can continue with the rest
            rtypes = suits.objects.filter(id=sku)
            return render(request,'suite.html', {'rtypes' : rtypes})
