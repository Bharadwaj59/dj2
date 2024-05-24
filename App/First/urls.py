from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
path('home', views.home, name='home'),
path('about', views.about, name='about'),
path('departments', views.departments, name='department'),
path('doctors', views.doctors, name='doctors'),
path('contact', views.contact, name='contact'),
path('afterabout', views.afterabout, name='afterabout'),
path('afterdepartments', views.afterdepartments, name='afterdepartment'),
path('afterdoctors', views.afterdoctors, name='afterdoctors'),
path('aftercontact', views.aftercontact, name='aftercontact'),
path('touch', views.touch, name='touch'),
path('anduku', views.signup, name='cha'),
path('signup', views.signup, name='signup'),
path('signupo', views.sign, name='signupyes'),
path('login', views.login, name='login'),
path('log', views.log, name='log'),
path('book', views.book, name='book'),
path('showmore', views.showmore, name='show'),
path('forgot', views.forgot, name='forgot'),
path('for', views.fors, name='for'),
path('otp', views.otp, name='otp'),
path('enter', views.enterotp, name='enterotp'),
path('entered', views.entered, name='entered'),
path('thank', views.tan, name='thank'),
path("updatepass",views.checknewpass,name="checknew"),
path("recoverypass",views.recoverypass,name="recovery"),
path("send_otp",views.send_otp,name="send otp"),

]