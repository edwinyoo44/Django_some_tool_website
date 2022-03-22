"""website_configs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app_api import views as app_api_views
from app_tool import views as app_tool_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.home),
    # tool頁面相關
    path('', app_tool_views.index),
    path('tool/bmi/<type>', app_tool_views.bmi),
    path('tool/temperature/<type>', app_tool_views.temperature),
    path('tool/exchangeRate/<type>', app_tool_views.exchangeRate),
    
    # API相關
    path('api/bmi/<type>', app_api_views.bmi),
    path('api/temperature/<type>', app_api_views.temperature),
    path('api/exchangeRate/<type>', app_api_views.exchangeRate),
]
