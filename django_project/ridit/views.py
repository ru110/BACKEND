from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import School,Contact
from .models import Partner
from .models import Puc,Chauffer
from .forms import DriveForm
from .forms import PartnerForm
from .forms import ChaufferForm
from .forms import PucForm
# Create your views here.
def home(request):
    if request.method == 'POST' and 'ContactForm' in request.POST:
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        phone = request.POST.get('phone')

        contact.name = name
        contact.email = email
        contact.comment = comment
        contact.phone = phone
        contact.save()
        return render(request,'ridit/success.html')
	
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

@login_required
def chauffer(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ChaufferForm()
        else:
            employee = Chauffer.objects.get(pk=id)
            form = ChaufferForm(instance=employee)
        return render(request, "ridit/chauffer.html", {'form': form})
    else:
        if id == 0:
            form = ChaufferForm(request.POST)
        else:
            employee = Chauffer.objects.get(pk=id)
            form = ChaufferForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            day = request.POST['days']
            total = 499 * int(day)
            # messages.success(request, 'Your request is submitted successfully')
            return render(request,"ridit/ch.html",{'total':total})
        else:
            # messages.error(request,'error')
            return render(request, "ridit/chauffer.html", {'form': form})

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
            vtype = request.POST['vehicle_type']
            total = 0
            if vtype=='2w':
                total=50
            elif vtype=='3w':
                total=150
            elif vtype=='4w':
                total=200
            elif vtype=='4cw':
                total=250
            else:
                total=500
            # messages.success(request, 'Your request is submitted successfully')
            return render(request,"ridit/p1.html",{'total':total})
        else:
            # messages.error(request,'error')
            return render(request, "ridit/puc.html", {'form': form})



def faq(request):
    return render(request,"faq/Main.html")

def driveFAQ(request):
    return render(request,"faq/driveFAQ.html")
def pucFAQ(request):
    return render(request,"faq/pucFAQ.html")

def chauffeurFAQ(request):
    return render(request,"faq/chauffeurFAQ.html")

def LicenseFAQ(request):
    return render(request,"faq/licenseFAQ.html")

def comming_soon(request):
    return render(request,"ridit/soon.html")
