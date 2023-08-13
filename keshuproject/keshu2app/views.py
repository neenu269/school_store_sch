from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from keshuapp.models import Place, Name


# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'login2.html')
        else:
            messages.info(request,"invalid credientials")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method =="POST":
        username=request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password= request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
                user.save();
                return redirect('login')

        else:

           messages.info(request,"password not matching")
           return redirect('register')
        return redirect('/')

    return render(request,"register.html")

def add(request):

        if request.method == "POST":
            name = request.POST.get('name', )
            dep = request.POST.get('dep', )
            year = request.POST.get('year', )

            movie = Place(name=name)
            return render(request, 'form2.html')

        return render(request, 'add.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
