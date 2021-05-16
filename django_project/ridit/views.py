from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import School
from .forms import DriveForm
# Create your views here.
def home(request):
	return render(request,'ridit/home.html')
	
@login_required
def school(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DriveForm()
        else:
            employee = School.objects.get(pk=id)
            form = DriveForm(instance=employee)
        return render(request, "ridit/school.html", {'form': form})
    else:
        if id == 0:
            form = DriveForm(request.POST)
        else:
            employee = School.objects.get(pk=id)
            form = DriveForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Your request is submitted successfully')
            return redirect('/success')
        else:
            # messages.error(request,'error')
            return render(request, "ridit/school.html", {'form': form})

def success(request):
    return render(request,"ridit/success.html")