"""photo URL Configuration

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
from django.urls import path
from apphoto import views as photo_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('home/', photo_views.home, name='home'),
    path('post/', photo_views.post, name='post'),
    path('add/', photo_views.client, name='add'),
    path('slide/', photo_views.slider, name='slide'),
    path('sucsess/', photo_views.sucsess, name='sucsess'),
    path('me/', photo_views.me, name='me'),
    path('qa/', photo_views.QA, name='qa'),
    path('thank/', photo_views.thank, name='thank')
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)