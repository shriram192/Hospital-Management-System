from django.urls import include, path

from django.contrib.auth import views as auth_views
from . import views

app_name = 'patient'

urlpatterns = [
    path('login/', views.login_view ,name='login'),
    path('info/',views.info,name='info'),
    path('logout/',views.logout_view,name='logout'),
]