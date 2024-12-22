from django.shortcuts import render,HttpResponseRedirect
from .froms import StudentRegistration
from .models import User
# from django.http import HttpResponseRedirect

# Create your views here.

# This function will add items and Show items
def add_show(request):
    if request.method == "POST":
        fd = StudentRegistration(request.POST)
        if fd.is_valid():
            nm = fd.cleaned_data["name"]
            eml = fd.cleaned_data["email"]
            pwd = fd.cleaned_data["password"]
            reg = User(name = nm, email = eml, password = pwd)
            reg.save()
            fd = StudentRegistration() # this line represents blank form after submitting form 
            
    else:
        fd = StudentRegistration()
        
    stud = User.objects.all()       
    return render(request,"enroll/addandshow.html",{"form":fd,"stu":stud})

# This function will Update/Edit selected data
def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(instance=pi)
    
    return render(request,"enroll/updatestudent.html",{"form":fm}) 
        


# This function will Delete selected data
def delete_data(request,id):
    if request.method == "POST":
        remove_data = User.objects.get(pk=id)
        remove_data.delete()
        return HttpResponseRedirect("/")