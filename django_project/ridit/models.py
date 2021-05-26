from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

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

class School(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  mobile = models.CharField(max_length=10,validators=[phone_regex])
  vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
  CHOICE = (('0','Male'),('1','Female'))
  gender = models.CharField(max_length=10,choices = CHOICE)
  DAYS = (('0','7 days'),('1','15 days'))
  days = models.CharField(max_length=10,choices = DAYS)
  date = models.DateField()
  city = models.ForeignKey(City,on_delete=models.CASCADE)

  def __str__(self):
      return self.name


class Service(models.Model):
  id = models.IntegerField(primary_key=True, unique = True)
  title = models.CharField(max_length=50,unique=True)

  def __str__(self):
    return self.title

class Partner(models.Model):
  name = models.CharField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  contact = models.CharField(max_length=10,validators=[phone_regex])
  service = models.ForeignKey(Service,on_delete=models.CASCADE)
  city = models.CharField(max_length=350)
  query = models.TextField(max_length=300)
  def __str__(self):
    return self.name

class Chauffer(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  contact = models.CharField(max_length=10,validators=[phone_regex])
  address = models.CharField(max_length=400)
  date = models.DateField()
  pincode = models.CharField(max_length=6)
  days = models.CharField(max_length=2)
  price = models.IntegerField()
  
  def __str__(self):
    return self.name
  
  @property
  def get_price(self):
    day = int(self.days)
    return 499*day
  


  def save(self, *args, **kwargs):
    self.price = self.get_price
    super(Chauffer, self).save(*args, **kwargs)
  


class Puc(models.Model):
  name = models.CharField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  contact = models.CharField(max_length=10,validators=[phone_regex])
  vehicle_no = models.CharField(max_length=20)
  exp_date = models.DateField()
  city = models.ForeignKey(City,on_delete=models.CASCADE)
  def __str__(self):
      return self.name