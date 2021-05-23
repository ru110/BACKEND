from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='ridit-home'),
  path('',views.school,name='school'),
  path('',views.partner,name='partner'),
  path('',views.chauffer,name='chauffer'),
  path('',views.puc,name='puc'),
   path('',views.ch,name='ch'),
  path('success/',views.success,name='success'),
]