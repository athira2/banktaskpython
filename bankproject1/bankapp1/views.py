
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render,redirect
from .models import Register,Form
# Create your views here.

def home(request):
    obj=Register.objects.all()
    obj1=Form.objects.all()

    return render(request,'home.html')
def user(request):

    return render(request,'user.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        cpassword=request.POST.get('cpassword','')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register.html')

            else:
                user = User.objects.create_user(username=username, password=password)

                user.save();
                return render(request, 'login.html')
                # print("user created")
        else:
            messages.info(request, "password not matching")
            return render(request, 'register.html')
        return redirect('/')
    return render(request,'register.html')





        # if password==cpassword:
        #     user=Register(username=username,password=password,cpassword=cpassword)
        #     user.save();
        #     return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'new.html')
        else:

            messages.info(request,"Invalid credentials")
            return render(request,"login")

    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        dob=request.POST.get('dob','')
        age=request.POST.get('age','')
        gender=request.POST.get('gender','')
        phonenumber=request.POST.get('phonenumber')
        mailid=request.POST.get('mailid','')
        address=request.POST.get('address','')
        district=request.POST.get('district','')
        branches=request.POST.get('branches','')
        accounttype=request.POST.get('accounttype','')
        materials=request.POST.get('materials','')
        form=Form(name=name, dob=dob, age=age, gender=gender, phonenumber=phonenumber,mailid=mailid , address=address, district=district, branches=branches, accounttype=accounttype,materials=materials)
        form.save();
        return render(request,'user.html')

    return render(request,'form.html')


