from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact
# Create your views here.
def custom(request):
  if request.method == 'POST':
    contact = Contact()
    name = request.POST.get('Name')
    email = request.POST.get('Email')
    comment = request.POST.get('Comment')
    contact.name = name
    contact.email = email
    contact.comment = comment
    contact.save()
    return HttpResponse("<h1>Thanks for reaching to us</h1>")

  return render(request,'demo/custom.html')
