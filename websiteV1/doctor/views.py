from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from landing.models import Type
from django.contrib import messages
from .models import Patient
from .models import Doctor
from landing.models import Type
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        if username is not None and password is not None:
            #login user
            user = authenticate(username = username,password=password)
            auth = Type.value.filter(type='doctor',username=user)
            if user is not None and len(auth) != 0:
                login(request,user)
                return redirect('doctor:dashboard')
            else:
                messages.error(request,'Incorrect Username or Password')
    return render(request,'doctor/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        if username != '' and password != '':
            user = User.objects.create_user(username=username,password=password)
            user.save()
            t = Type(username=username,type='doctor')
            t.save()
            doc = Doctor(name=username)
            doc.save()
            return render(request,'doctor/login.html')
        else:
            messages.error(request,'Please enter all fields')

    return render(request, 'doctor/signup.html')
def success(request):
    return render(request,'doctor/success.html')

@login_required
def dashboard(request):
    current = request.user.username
    foreign = Doctor.value.get(name=current).pk
    patients = Patient.value.filter(doctor=foreign)
    context = {'patients':patients}
    return render(request,'doctor/dashboard.html',context)

@login_required
def addPatient(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            bg = request.POST['bg']
            age = request.POST['age']
            desc = request.POST['desc']
            current_user = request.user.username
            foreign = Doctor.value.get(name=current_user)
            p = Patient(name=name,bg=bg,age=age,desc=desc,doctor=foreign)
            p.save()
            user = User.objects.create_user(username=name,password='1234')
            user.save()
            type = Type(username=name,type='patient')
            type.save()
            patients = Patient.value.filter(doctor = foreign)
            context = {'patients':patients}
            return render(request,'doctor/dashboard.html',context)
        except:
            current_user = request.user.username
            foreign = Doctor.value.get(name=current_user)
            patients = Patient.value.filter(doctor = foreign)
            context = {'patients':patients}
            return render(request,'doctor/dashboard.html',context)


@login_required
def removePatient(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            patient = Patient.value.filter(name=name)
            User.objects.filter(username=name).delete()
            patient.delete()
            Type.value.filter(username=name).delete()
            current = request.user.username
            foreign = Doctor.value.get(name=current) 
            patients = Patient.value.filter(doctor = foreign)
            context = {'patients':patients}
            return render(request,'doctor/dashboard.html',context)
        except:
            current = request.user.username
            foreign = Doctor.value.get(name=current) 
            patients = Patient.value.filter(doctor = foreign)
            context = {'patients':patients}
            return render(request,'doctor/dashboard.html',context)
     
@login_required
def updatePatient(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            current_patient = Patient.value.get(name=name)
        except:
            foreign = Doctor.value.get(name=request.user.username)
            patients = Patient.value.filter(doctor = foreign)
            context = {'patients':patients}
            return render(request,'doctor/dashboard.html',context)
        try:
            age = request.POST['age']
            current_patient.age=age
            current_patient.save()
        except:
            try:
                bg = request.POST['bg']
                current_patient.bg = bg
                current_patient.save()
            except:
                try:
                    desc = request.POST['desc']
                    current_patient.desc = desc    
                    current_patient.save()
                except:
                    foreign = Doctor.value.get(name=request.user.username)
                    patients = Patient.value.filter(doctor = foreign)
                    context = {'patients':patients}
                    return render(request,'doctor/dashboard.html',context)
        foreign = Doctor.value.get(name=request.user.username)
        patients = Patient.value.filter(doctor = foreign)
        context = {'patients':patients}
        return render(request,'doctor/dashboard.html',context)
        

def logout_view(request):
        logout(request)
        return render(request,'landing/index.html')