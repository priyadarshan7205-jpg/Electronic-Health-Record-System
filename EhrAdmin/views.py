from django.shortcuts import render,redirect
from Register.models import Register_Master
from EhrAdmin.models import adminprofile_master
from Patient.models import *


from .models import Register_Master
def viewdata(request):
    ob=Register_Master.objects.all()
    if request.method=="POST":
        email=request.POST["email"]
        btn=request.POST["btn"]
        if btn=="delete":
            Register_Master.objects.get(Email=email).delete()
            return  redirect("viewdata")
        if btn=="edit":
            data=Register_Master.objects.get(Email=email)
            return render(request,"edit.html",{'user':data})
        if btn=="billgenerate":
            billdata=Register_Master.objects.get(Email=email)
            patient = Register_Master.objects.get(Email=email)
            report = PatientTestReport.objects.filter(patient=patient).last()
            if not report:
                return render(request, 'billgenerate.html', {"error": "No bill found for this patient!"})
            tests = report.tests.all()
            total = report.total_price
            return render(request,"billgenerate.html",{'email':billdata,"patient": patient,"tests": tests,
        "total": total,
        "report": report,})
    return render(request,'viewdata.html',{'data':ob})

def generatebill(request, email):
    


 
   

    return render(request, "billgenerate.html", {
        
    })



    
    

def adminviewprofile(request):
    email=request.session.get('email')
    ob=Register_Master.objects.get(Email=email)
    ob1=adminprofile_master.objects.get(email=ob)

    return render(request,'adminviewprofile.html',{'data':ob,'data1':ob1})
def adminprofile(request):
    email=request.session.get('email')
    ob=Register_Master.objects.get(Email=email)
    if request.method=="POST":
        image_file=request.FILES['image']
        
        doc_file=request.FILES['uploaded_doc']
        profile_update_obj,created=adminprofile_master.objects.get_or_create(email=ob)
       
        if image_file:
            profile_update_obj.Image=image_file
        if doc_file:
            profile_update_obj.Document=doc_file
        profile_update_obj.save() 
        ob.Name=request.POST.get('name',ob.Name)
        ob.Email=request.POST.get('email',ob.Email)
        ob.Mobile=request.POST.get('mobile',ob.Mobile)
        ob.Password=request.POST.get('pwd',ob.Password)
        ob.Address=request.POST.get('ads',ob.Address)
        ob.DOB=request.POST.get('dob',ob.DOB)
        ob.Gender=request.POST.get('gender',ob.Gender)
        ob.save()
        return redirect('adminprofile')
    return render(request,'adminprofile.html',{'adata':ob})


def update(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        status=request.POST["status"]
        Register_Master.objects.filter(Email=email).update(Name=name,Mobile=mobile,Gender=gender,
                                                           Address=address,status=status)
        return redirect("viewdata")
    return render(request,"edit.html")

def ahome(request):
    username=request.session.get('name')
    return render(request,'ahome.html',{'aname':username})