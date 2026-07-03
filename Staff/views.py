from django.shortcuts import render
from Register.models import Register_Master
from .forms import testForm
from Patient.models import *
# Create your views here.
def applytest(request):
    ob=PatientTestReport.objects.all()
    return render(request,"applytest.html",{'rdata':ob})

def add_test(request):
    formobj=testForm()
    if request.method=="POST":
        formobj=testForm(request.POST)
        if formobj.is_valid():
            formobj.save()
    return render(request,'Add_test.html',{'form':formobj})

def d_p_viewdata(request):
    ob=Register_Master.objects.filter(Role_Name="Doctor")
    ob1=Register_Master.objects.filter(Role_Name="Patient")

    return render(request,"patient_doctor_data.html",{'data':ob,"data1":ob1})
def shome(request):
    username=request.session.get('name')
    return render(request,'shome.html',{'sname':username}) 