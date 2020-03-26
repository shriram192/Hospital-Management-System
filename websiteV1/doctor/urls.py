from django.urls import include, path

from django.contrib.auth import views as auth_views
from . import views

app_name = 'doctor'

urlpatterns = [
    path('login/', views.login_view ,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addPatient/',views.addPatient,name='add'),
    path('removePatient/',views.removePatient,name='remove'),
    path('updatePatient/',views.updatePatient,name='update'),
    path('logout/',views.logout_view,name='logout')
]