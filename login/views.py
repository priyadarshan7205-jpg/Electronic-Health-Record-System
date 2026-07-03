from django.shortcuts import render,redirect
from Register.models import Register_Master

# Create your views here.
def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        pwd=request.POST["pwd"]
        try:
            ob=Register_Master.objects.get(Email=email,Password=pwd)
            request.session['name']=ob.Name
            request.session['email']=ob.Email

            if ob.status==1:
                if ob.Role_Name=="Doctor":
                    return redirect('dhome')
                elif ob.Role_Name=="Patient":
                    return redirect('phome')
                elif ob.Role_Name=="Staff":
                    return redirect('shome')
                elif ob.Role_Name=="EhrAdmin":
                    return redirect("ahome")
            else:
                return render(request,"login.html",{'msg':"Waiting for admin conformation!!!!!"})   
        except Exception as e:
            return render(request,"login.html",{"msg":'invalid  '  + str(e)})
    return render(request,"login.html")