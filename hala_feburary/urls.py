"""hala_feburary URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from users.views import user_login , user_register, logout_view
from events.views import info, event_detail, event_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('events/', event_list, name='event_list'),
    path ('<int:pk>/',event_detail, name='event_detail'),
    path('info/' ,info, name='info'),
    path('login/' , user_login, name= 'login' ),
    path('register/',user_register, name= 'register'),
    path('logout/',logout_view, name= 'logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)