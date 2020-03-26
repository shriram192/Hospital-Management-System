from django.db import models
from administrator.models import Node
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from landing.models import Type
from .models import Node
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        if username is not None and password is not None:
            #login user
            user = authenticate(username = username,password=password)
            auth = Type.value.filter(type='admin',username=user)
            if user is not None and len(auth) != 0:
                login(request,user)
                nodes = Node.value.all()
                newNodes = []
                for i in nodes:
                    newNodes.append([i, str(i.nid)+'State', str(i.isActive)])
                context = {'nodes':newNodes}
                return render(request,'administrator/adminDashboard.html',context)
            else:
                messages.error(request,'Invalid Username or Password')
    return render(request,'administrator/login.html')
        
def logout_view(request):
        logout(request)
        return render(request,'landing/index.html')
#new view added for admindashboard

def dashboard(request):
    nodes = Node.value.all()
    newNodes = []
    for i in nodes:
        newNodes.append([i, str(i.nid)+'State', str(i.isActive)])
    context = {'nodes':newNodes}
    return render(request,'administrator/adminDashboard.html',context)

@login_required
def addNode(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            mc = request.POST['mc']
            s1 = request.POST['s1']
            s2 = request.POST['s2']
            s3 = request.POST['s3']
            s4 = request.POST['s4']
            s5 = request.POST['s5']
            isActive = request.POST['switch']
            if name != '' and mc != '' and s1 != '' and s2 != '' and s3 != '' and s4 != '' and s5 != '':
                n = Node(name=name,mc=mc,s1=s1,s2=s2,s3=s3,s4=s4,s5=s5,isActive=isActive)
                n.save()
            nodes = Node.value.all()
            newNodes = []
            for i in nodes:
                newNodes.append([i, str(i.nid)+'State', str(i.isActive)])
            context = {'nodes':newNodes}
            return render(request,'administrator/adminDashboard.html',context)
        except:
            nodes = Node.value.all()
            newNodes = []
            for i in nodes:
                newNodes.append([i, str(i.nid)+'State', str(i.isActive)])
            context = {'nodes':newNodes}
            return render(request,'administrator/adminDashboard.html',context)

@login_required
def removeNode(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            node = Node.value.get(name=name)
            node.delete() 
            nodes = Node.value.all()
            newNodes = []
            for i in nodes:
                newNodes.append([i, str(i.nid)+'State', str(i.isActive)])
            context = {'nodes':newNodes}
            return render(request,'administrator/adminDashboard.html',context)
        except:
            nodes = Node.value.all()
            newNodes = []
            for i in nodes:
                newNodes.append([i, str(i.nid)+'State', str(i.isActive)])
            context = {'nodes':newNodes}
            return render(request,'administrator/adminDashboard.html',context)

@login_required
def updateNode(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            current_node = Node.value.get(name=name)
        except:
            nodes = Node.value.all()
            newNodes = []
            for i in nodes:
                newNodes.append([i, str(i.nid)+'State', str(i.isActive)])
            context = {'nodes':newNodes}
            return render(request,'administrator/adminDashboard.html',context)
        try:    
            isActive = request.POST['switch']
            column = request.POST['type']
            value = request.POST['value']
            current_node.isActive = isActive
            current_node.save()
            if column == 'Microcontroller':
                current_node.mc = value
                current_node.save()
            elif column == 'S1':
                current_node.s1 = value
                current_node.save()
            elif column == 'S2':
                current_node.s2 = value
                current_node.save()
            elif column == 'S3':
                current_node.s3 = value
                current_node.save()
            elif column == 'S4':
                current_node.s4 = value
                current_node.save()
            elif column == 'S5':
                current_node.s5 = value
                current_node.save()
            nodes = Node.value.all()
            newNodes = []
            for i in nodes:
                newNodes.append([i, str(i.nid)+'State', str(i.isActive)])
            context = {'nodes':newNodes}
            return render(request,'administrator/adminDashboard.html',context)
        except:
            nodes = Node.value.all()
            newNodes = []
            for i in nodes:
                newNodes.append([i, str(i.nid)+'State', str(i.isActive)])
            context = {'nodes':newNodes}
            return render(request,'administrator/adminDashboard.html',context)


        