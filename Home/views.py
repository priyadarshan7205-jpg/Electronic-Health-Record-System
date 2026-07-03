from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def gallary(request):
    return render(request,"gallary.html") 
def faq(request):
    return render(request,"faq.html")
def add(request):
    if request.method=="POST":
        a=request.POST["fno"]
        b=request.POST["sno"]
        result=int(a)+int(b)
        return render(request,"add.html",context={"res":result})
    return render(request,"add.html")
def calculator(request):
    result=0
    if request.method=="POST":
        a=request.POST["fno"]
        b=request.POST["sno"]
        btn=request.POST["btn"]
        if btn=="ADD":
            result=int(a)+int(b)
        elif btn=="SUB":
            result=int(a)-int(b)
        elif btn=="MUL":
            result=int(a)*int(b)
        elif btn=="DIV":
            result=int(a)//int(b)        
    return render(request,"calculator.html",{"res":result})


def index(request):
    return HttpResponse("<h1>welcome to Django's World!!!!!</h1>")


from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, message=message)

        return render(request, "contact.html", {"msg": "Message sent successfully!"})

    return render(request, "contact.html")


def live_chat(request):
    return render(request, "copilot_chat.html")



