from django.shortcuts import render
from django.contrib import messages
from .models import Contact

# Create your views here.
def index(request):
   if request.method == 'POST' :
      fullname=request.POST['fullname']
      email=request.POST['email']
      message=request.POST['message']
      obj=Contact(fullname=fullname,email=email,message=message)
      obj.save()


   return render(request,'pages/index.html')

def showContact(request):
   showinfo = Contact.objects.all()
   context={
      'showinfo' : showinfo,
   }
   
       
   return render(request,'pages/showinfo.html',context)

