from django.db import models

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from landing.models import Type
from django.contrib import messages
from doctor.models import Patient
from doctor.models import Doctor
# Create your views here.



def login_view(request):
    if request.method == 'POST':
        username = request.POST['user']
        if username is not None:
            #login user
            user = authenticate(username = username,password='1234')
            auth = Type.value.filter(type='patient',username=user)
            if user is not None and len(auth) != 0:
                login(request,user)
                return redirect('patient:info')
            else:
                messages.error(request,'Patient not present')
    return render(request,'patient/login.html')

def info(request):
        name = request.user.username
        info = Patient.value.get(name=name)
        doc = Doctor.value.get(name = info.doctor.name )
        context = { 'name': info.name,'id': info.pid , 'age': info.age , 'bg': info.bg ,'desc': info.desc , 'doctor': doc.name}
        return render(request,'patient/info.html', context)





def logout_view(request):
        logout(request)
        return render(request,'landing/index.html')