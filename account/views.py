from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def choose(request):
    return render(request,'choose.html')

def owner_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #push data to RDBMS
        if password1==password2 :
            if User.objects.filter(username=username).exists():
                return render(request,'owner_register.html.html',{'massage_username':'username taken..'})
            elif User.objects.filter(email=email).exists():
                return render(request,'owner_register.html',{'massage_email':'email taken..'})
            else:
                user= User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return render(request,'owner_register.html',{'massage':True})
                return render(request,'login.html')
        else:
            return render(request,'owner_register.html',{'massage_password':'email taken..'})
        return redirect('/')
    else:
        return render(request,'owner_register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credential')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):

    #fetch data
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #push data to RDBMS
        if password1==password2 :
            if User.objects.filter(username=username).exists():
                return render(request,'register.html',{'massage_username':'username taken..'})
            elif User.objects.filter(email=email).exists():
                return render(request,'register.html',{'massage_email':'email taken..'})
            else:
                user= User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return render(request,'login.html')
        else:
            return render(request,'register.html',{'massage_password':'password not maching..'})
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')