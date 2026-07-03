from django.urls import path
from Patient.views import testreport,viewlabtest,phome,dviewdata,patientprofile,patientviewprofile,success,take_appointment,patient_dashboard
urlpatterns = [
    path('',phome,name="phome"),
    path('dviewdata',dviewdata,name='dviewdata'),
    path('patientprofile',patientprofile,name="patientprofile"),
    path('patientviewprofile',patientviewprofile,name="patientviewprofile"),
    path('success',success,name="success"),
    path('take_appointment',take_appointment,name="take_appointment"),
    path('patient_dashboard',patient_dashboard,name='patient_dashboard'),
    path('viewlabtest',viewlabtest,name="viewlabtest"),
    path("testreport/", testreport, name="testreport"),


]