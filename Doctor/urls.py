from django.urls import path
from Doctor.views import viewdetails,dhome,pviewdata,display_appointment,approve_appointment,cancel_appointment
urlpatterns = [
    path('',dhome,name="dhome"),
    path('pviewdata/',pviewdata,name='pviewdata'),
    path('display_appointment/',display_appointment,name="display_appointment"),
    path('approve_appointment/', approve_appointment, name='approve_appointment'),
    path('cancel_appointment/', cancel_appointment, name='cancel_appointment'),
    path('viewdetails',viewdetails,name="viewdetails"),
]