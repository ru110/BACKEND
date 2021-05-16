from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from demo import views as demo_views
from ridit import views as ridit_views
#from employee_reg import views as emp_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('ridit.urls')),
    path('school/', ridit_views.school, name='school'),
    path('custom/', demo_views.custom , name='custom'),
    #path('empform/',emp_views.empform,name='empform'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),#for datepicker functionality in forms
]

