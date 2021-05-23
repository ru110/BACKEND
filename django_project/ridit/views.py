from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import School
from .models import Partner
from .forms import DriveForm
from .forms import PartnerForm
from .forms import ChaufferForm
from .forms import PucForm
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

def ch(request):
    return render(request,"ridit/ch.html")

@login_required
def partner(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PartnerForm()
        else:
            employee = Partner.objects.get(pk=id)
            form = PartnerForm(instance=employee)
        return render(request, "ridit/partner.html", {'form': form})
    else:
        if id == 0:
            form = PartnerForm(request.POST)
        else:
            employee = Partner.objects.get(pk=id)
            form = PartnerForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Your request is submitted successfully')
            return redirect('/success')
        else:
            # messages.error(request,'error')
            return render(request, "ridit/partner.html", {'form': form})
'''
@login_required
def chauffer(request, id=0):
    if request.method == "GET":
        #days = request.GET['days']
        total = 499 * 1
        if id == 0:
            form = ChaufferForm()
        else:
            employee = Chauffer.objects.get(pk=id)
            form = ChaufferForm(instance=employee)
        return render(request, "ridit/chauffer.html", {'form': form,'total':total})
    else:
        #days= request.POST['days']
        total = 499 * 1
        if id == 0:
            form = ChaufferForm(request.POST)
        else:
            employee = Chauffer.objects.get(pk=id)
            form = ChaufferForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Your request is submitted successfully')
            return redirect('/success')
        else:
            # messages.error(request,'error')
            return render(request, "ridit/chauffer.html", {'form': form,'total':total})'''

@login_required
def chauffer(request):
    if request.method=='POST':
        form = ChaufferForm(request.POST)
        if form.is_valid():
            form.save()
            day = request.POST['days']
            total = 499 * int(day)
            name = request.POST['name']
            return render(request,"ridit/ch.html",{'name':name,'total':total})
    else:
        form = ChaufferForm()
        return render(request,"ridit/chauffer.html",{'form':form})

@login_required
def puc(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PucForm()
        else:
            employee = Puc.objects.get(pk=id)
            form = PucForm(instance=employee)
        return render(request, "ridit/puc.html", {'form': form})
    else:
        if id == 0:
            form = PucForm(request.POST)
        else:
            employee = Puc.objects.get(pk=id)
            form = PucForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Your request is submitted successfully')
            return redirect('/success')
        else:
            # messages.error(request,'error')
            return render(request, "ridit/puc.html", {'form': form})