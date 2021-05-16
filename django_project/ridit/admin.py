from django.contrib import admin

from .models import School
from .models import Gender
from .models import Vehicle
from .models import City
# Register your models here.

admin.site.register(School)
admin.site.register(Gender)
admin.site.register(Vehicle)
admin.site.register(City)