"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required
from project.middleware import ipSet
# authenticate, login, 

@staff_member_required
def ipsView(request):
    template = 'ips.html'
    context = {'ips': ipSet}
    return render(request, template, context)

def home(request):
    # home template
    template = 'home.html' 
    return render(request, template)

def logoutUser(request):
    logout(request) 
    return redirect('home')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('portafolio/', include('project.urls')),
    path('', home, name = 'home'),
    path('logout', logoutUser, name = 'logout'),
    path('ips/', ipsView, name = 'ips'),
]
    # path('', include('user.urls')),

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
