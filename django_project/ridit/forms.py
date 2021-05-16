from django import forms
from .models import School
from django.contrib.admin import widgets  

class DriveForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ('name','mobile','email','vehicle','gender','date','city')
        labels = {
            'name':'Full Name',
            'email':'Email Id',
            'mobile':'Mobile No',
            'vehicle' : 'Which vehicle you want to learn?',
            'date' : 'Date',
            'city' : 'City'
        }

    def __init__(self, *args, **kwargs):
        super(DriveForm,self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['city'].empty_label = "Select"
        self.fields['vehicle'].empty_label = "Select"
        self.fields['date'].widget = widgets.AdminDateWidget()