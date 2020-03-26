from django.urls import include, path

from django.contrib.auth import views as auth_views
from . import views

app_name = 'administrator'

urlpatterns = [
    path('login/', views.login_view ,name='login'),
    path('addNode/',views.addNode,name='addNode'),
    path('updateNode/',views.updateNode,name='updateNode'),
    path('removeNode/',views.removeNode,name='removeNode'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout_view,name='logout'),
]