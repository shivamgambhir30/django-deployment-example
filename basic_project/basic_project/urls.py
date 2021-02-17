"""basic_project URL Configuration

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
from basic_project_app import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
urlpatterns = [
path('home',views.index,name="template1"),   #//homepage
path('logout/',views.user_logout,name="template3"),
path('fillform/',views.register,name="template2"),
path('basic_project_app/',include('basic_project_app.urls',namespace="basic_project_app")),
path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
