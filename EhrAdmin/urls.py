from django.urls import path
from EhrAdmin.views import *
urlpatterns = [
    path('',ahome,name="ahome"),
    path('viewdata/',viewdata,name="viewdata"),
    path("update/",update,name="update"),
    path("adminprofile/",adminprofile,name="adminprofile"),
    path('adminviewprofile',adminviewprofile,name="adminviewprofile"),
    # path('bill/', billamount, name="billamount"),
    path('generatebill/<str:email>/', generatebill, name="generatebill"),


]