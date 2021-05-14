from django.db import models

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  mobile = models.CharField(max_length=15)
  vehicle = models.CharField(max_length=50)
  gender = models.CharField(max_length=10)
  date = models.DateField()
  city = models.CharField(max_length=100)

  def __str__(self):
    return self.name