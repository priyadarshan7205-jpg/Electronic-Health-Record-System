"""
URL configuration for EHR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Home import views as hviews
from django.urls import path,include
from django.conf import settings     #added new line
from django.conf.urls.static import static
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Register
    path('register/', include('Register.urls')),
    #login
    path('login/', include('login.urls')),
    #staff
    path('staff/',include('Staff.urls')),
    #patient
    path('patient/',include('Patient.urls') ),
    #doctor
    path('doctor/',include('Doctor.urls') ),
    #ehradmin
    path('ehradmin/',include('EhrAdmin.urls') ),

    


    
    #Home
    path('',hviews.home,name="home"),
    path('about/',hviews.about,name="about"),
    path('contact/',hviews.contact,name="contact"),
    path('gallary/',hviews.gallary,name="gallary"),
    path('faq/',hviews.faq,name="faq"),
    path('live-chat/', hviews.live_chat, name="live-chat"),
    path('add/',hviews.add,name="add"),
    path('calculator/',hviews.calculator,name="calculator"),



    # path('index/',hviews.index,name="index"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
