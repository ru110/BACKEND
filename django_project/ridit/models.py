from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.
# def validate_mail(value):
#     if "@gmail.com" in value:
#         return value
#     else:
#         raise ValidationError("This field accepts mail id of google only")

class Gender(models.Model):
	id = models.IntegerField(primary_key=True,unique=True)
	title = models.CharField(max_length=50,unique=True)

	def __str__(self):
		return self.title

class Vehicle(models.Model):
  id = models.IntegerField(primary_key=True,unique =  True)
  title = models.CharField(max_length=50,unique=True)

  def __str__(self):
    return self.title

class City(models.Model):
  id = models.IntegerField(primary_key=True, unique = True)
  title = models.CharField(max_length=50,unique=True)

  def __str__(self):
    return self.title

# ,validators =[validate_mail]
class School(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  mobile = models.CharField(max_length=10,validators=[phone_regex])
  vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
  gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
  date = models.DateField()
  city = models.ForeignKey(City,on_delete=models.CASCADE)