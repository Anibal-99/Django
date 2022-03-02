"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import HomeView # de esta manera traemos las vistas que queremos y la que en este caso queremos es HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',HomeView.as_view(), name='home'), # sino ponemos el .as_view() nos va a salir un error porque HomeView es una clase

    path('blog/',include('blog.urls', namespace='blog'))
]
