from django.shortcuts import render,redirect
from Register.models import Register_Master
from datetime import datetime
from Staff.models import Laboratory_test
from .models import *


def viewlabtest(request):
    email = request.session.get("email")  
    logged_in_user = Register_Master.objects.get(Email=email)
    if request.method == "POST":
        selected_ids = request.POST.getlist("selected_tests")
        patient = logged_in_user  
        tests = Laboratory_test.objects.filter(test_id__in=selected_ids)
        total_price = sum(test.test_Price for test in tests)
        report = PatientTestReport.objects.create(patient=patient,total_price=total_price)
        report.tests.set(tests)
        report.save()
        request.session["last_report_id"] = report.report_id
        return redirect("testreport")
    ob = Laboratory_test.objects.all()
    return render(request, "viewlabtest.html", {"testdata": ob, "user": logged_in_user})


def testreport(request):
    report_id = request.session.get("last_report_id")
    report = PatientTestReport.objects.get(pk=report_id)

    return render(request, "testreport.html", {
        "report": report,
        "tests": report.tests.all(),
        "total_price": report.total_price
    })



from django.shortcuts import render, redirect
from .models import Doctor_Appointment, Register_Master

def patient_dashboard(request):
    
    email = request.session.get('email')

    if not email:  
        return redirect("login")   # redirect if not logged in

    try:
        # Find patient details using email
        patient = Register_Master.objects.get(Email=email)
        pmobile = patient.Mobile

        # Get appointments using the patient's mobile
        appointments = Doctor_Appointment.objects.filter(p_mobile=pmobile)
    except Register_Master.DoesNotExist:
        appointments = []

    return render(request, "patient_dashboard.html", {"msg": appointments})

def take_appointment(request):
    if request.method=="POST":
        doct_name=request.POST["dname"]
        doct_email=request.POST["demail"]
        demail=Register_Master.objects.get(Email=doct_email)
        doct_mobile=request.POST["dmobile"]
        p_name=request.POST['pname']
        p_mobile=request.POST['pmobile']
        p_email=request.POST['pemail']
        p_dob=request.POST['pdob']
        p_address=request.POST['paddress']
        p_gender=request.POST['pgender']
        diseases=request.POST["disease"]
        ob=Doctor_Appointment.objects.create(
                doct_name = doct_name,
                doct_contact =doct_mobile,
                doct_email = demail,
                p_name =p_name,
                p_mobile =p_mobile  ,
                p_address = p_address,
                p_gender = p_gender ,
                dob =p_dob,
                p_disease = diseases,

        )
        ob.save()
        return redirect("success")

    

    return render(request, "book_appointment.html")
def success(request):
    return render(request,"success_page.html")

def dviewdata(request):
    ob=Register_Master.objects.filter(Role_Name="Doctor")
    if request.method=="POST":
        demail=request.POST["email"]
        btn=request.POST["btn"]
        if btn=="Appointment":
            obj=Register_Master.objects.get(Email=demail)
            pemail=request.session.get('email')
            obj1=Register_Master.objects.get(Email=pemail)
            return render(request,"book_appointment.html",{'ddata':obj,'pdata':obj1})
    
    return render(request,'doctor_data.html',{'data':ob})




def phome(request):
    username=request.session.get('name')
    return render(request,'phome.html',{'pname':username})

def patientprofile(request):
    email=request.session.get('email')
    ob=Register_Master.objects.get(Email=email)
     
    if request.method=="POST":
        image_file=request.FILES['image']
        doc_file=request.FILES['uploaded_doc']
        diseases=request.POST['disesase']
        profile_update_obj,created=patientprofile_master.objects.get_or_create(email=ob)
       
        if image_file:
            profile_update_obj.Image=image_file
        if doc_file:
            profile_update_obj.Document=doc_file
        if diseases  :
            profile_update_obj.Diseases=diseases  
        profile_update_obj.save() 
        ob.Name=request.POST.get('name',ob.Name)
        ob.Email=request.POST.get('email',ob.Email)
        ob.Mobile=request.POST.get('mobile',ob.Mobile)
        ob.Password=request.POST.get('pwd',ob.Password)
        ob.Address=request.POST.get('ads',ob.Address)
        ob.DOB=request.POST.get('dob',ob.DOB)
        ob.Gender=request.POST.get('gender',ob.Gender)
        ob.save()
        return redirect('patientviewprofile')
    return render(request,"patientprofile.html",{'pdata':ob})


def patientviewprofile(request):
    email = request.session.get('email')   # patient logged-in email
    if not email:
        return redirect("login")

    try:
        pdata = Register_Master.objects.get(Email=email)
    except Register_Master.DoesNotExist:
        pdata = None

    return render(request, "patientviewprofile.html", {"pdata": pdata})