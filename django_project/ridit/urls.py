from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='ridit-home'),
  path('',views.schools,name='schools'),
]