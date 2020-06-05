"""College URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('satheesh/',views.home,name='home'),
    path('seenu/<str:name>/',views.home1,name='home1'),
    path('anil/<int:id>/',views.home2,name='home2'),
    path('registration/',views.register,name='register'),
    path('showdetails/',views.showdata,name='showdata'),
    path('home/',views.myhome,name='myhome'),
]





