"""Gopesa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

#IMPORTING LIBRARIES
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from principal import views

#------------------------- END IMPORT FILES--------------------------------------

#URL PATTERNS PROJECT
urlpatterns = [
    path('', views.index,name='index'), # SITE INDEX VIEW
    path('',include('principal.urls')), # URL APP PRINCIPAL
    path('admin/', admin.site.urls), # ADMIN VIEW
]

#------------------------- END URLS--------------------------------------

#APP NAME
app_name = 'principal'
