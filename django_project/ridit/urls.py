from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='ridit-home'),
  path('',views.school,name='school'),
  path('success/',views.success,name='success'),
]