from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import School
# Create your views here.
def home(request):
	return render(request,'ridit/home.html')

def schools(request):
	if request.method == 'POST':
		school = School()
		name = request.POST.get('Name')
		email = request.POST.get('Email')
		mobile = request.POST.get('Mobile')
		vehicle = request.POST.get('Vehicle')
		gender = request.POST.get('Gender')
		date = request.POST.get('Date')
		city = request.POST.get('City')
		
		school.name = name
		school.email = email
		school.mobile = mobile
		school.vehicle = vehicle
		school.gender = gender
		school.date = date
		school.city = city
		school.save()
		return redirect('/')

	return render(request,'ridit/school.html')