import math
import random

from django.core import mail
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,loader
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from .models import Members
from pymongo import MongoClient

r=0

client = MongoClient("mongodb://127.0.0.1:27017/")

db = client['Details']
coll = db.info

def index(request):
    template = loader.get_template('First/index.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('First/about.html')
    return HttpResponse(template.render())

def afterabout(request):
    template = loader.get_template('First/afterabout.html')
    return HttpResponse(template.render())

@csrf_exempt
def contact(request):
    template = loader.get_template('First/contact.html')
    return HttpResponse(template.render())

def departments(request):
    template = loader.get_template('First/departments.html')
    return HttpResponse(template.render())

def doctors(request):
    template = loader.get_template('First/doctors.html')
    return HttpResponse(template.render())


@csrf_exempt
def signup(request):
    template = loader.get_template('First/signup.html')
    return HttpResponse(template.render())


def aftercontact(request):
    template = loader.get_template('First/aftercontact.html')
    return HttpResponse(template.render())

def showmore(request):
    template = loader.get_template('First/showmore.html')
    return HttpResponse(template.render())

def afterdepartments(request):
    template = loader.get_template('First/afterdepartments.html')
    return HttpResponse(template.render())

def afterdoctors(request):
    template = loader.get_template('First/afterdoctors.html')
    return HttpResponse(template.render())


def forgot(request):
    template = loader.get_template('First/forget.html')
    return HttpResponse(template.render())

@csrf_exempt
def book(request):
    if request.method == "POST":
        e = request.POST.get('email')
        u=request.POST.get('name')
        i= request.POST.get('id')
        subject = 'Your Appoitment is Booked'
        o = generateOTP()
        html_message = render_to_string('First/thankyou.html', context={'email':e, 'name': u, 'id':id})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = [e, ]
        mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)
        return render(request, 'First/index.html')
    else:
        return HttpResponse('NOT')


@csrf_exempt
def fors(request):
    if request.method == "POST":
        e = request.POST.get('email')
        subject = 'Reset your password'
        message = 'Plese vist the url to change the password http://127.0.0.1:8000/recoverypass/ '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'First/signup.html')
    else:
        return HttpResponse('NOT')


def recoverypass(request):
    return render(request,"First/f.html")


@csrf_exempt
def sign(request):
    if request.method == "POST":
        u=request.POST.get('name')
        e = request.POST.get('email')
        password = request.POST.get('passw')
        db.coll.insert_one({'name': u,'email': e, 'passw': password})
        context={'name':u,'email':e,'phon':password,}
        return render(request,'First/index.html',context)
    else:
        return HttpResponse('NOT')

@csrf_exempt
def login(request):
    template = loader.get_template('First/signup.html')
    return HttpResponse(template.render())

def otp(request):
    template = loader.get_template('First/otp.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('First/home2.html')
    return HttpResponse(template.render())

def tan(request):
    template = loader.get_template('First/thankyou.html')
    return HttpResponse(template.render())


@csrf_exempt
def enterotp(request):
    template = loader.get_template('First/enterotp.html')
    return HttpResponse(template.render())

@csrf_exempt
def log(request):
    if request.method=='POST':
        global u
        u = request.POST.get('name')
        e = request.POST.get('email')
        password = request.POST.get('passw')
        c=db.coll.find_one({'email':e})
        subject = 'Your otp is to login'
        message = send_otp
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e]
        global  name

        name= c['name']
        context = {'name': c['name'], 'email': e, 'phon': password, }
        subject = 'Thank for your support'
        o = generateOTP()
        html_message = render_to_string('First/otp.html', context={'number': o, 'name': c['name']})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = [e, ]
        mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)
        if c['email']==e and c['passw']==password:

            return render(request,"First/enterotp.html",context)
        else:
            return render(request,"First/signup.html")
    else:
        pass

@csrf_exempt
def touch(request):
    if request.method == "POST":
        name=request.POST['name']
        p= request.POST['ph']
        email = request.POST['email']
        mssg=request.POST['mssg']
        subject = 'Thank for your support'
        o = generateOTP()
        html_message =render_to_string('First/otp.html', context={'number':o,'name':name})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = [email, ]
        mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)
        context={'name':name,'phon':p,'email':email,'mssg':mssg}
        return render(request,'First/touchit.html',context)
    else:
        return HttpResponse('NOT')



@csrf_exempt
def entered(request):

    if request.method == "POST":
        otp=request.POST.get('otp')
        if otp == r:
            return render(request,'First/home2.html',context={'name':name})
        return HttpResponse('Success')
    else:
        return HttpResponse('NOT')


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    global r
    r=OTP
    return r



def send_otp(request):
    email = request.GET.get("email")
    o = generateOTP()
    return render(request, 'First/otp.html', context={'number':o})


def checknewpass(request):
    if request.method=="POST":
        email=request.POST.get("email")
        passwo=request.POST.get("passw")
        c=db.coll.find_one({'email':email})
        if c["email"]==email:
            db.coll.update_one({"email":email},{"$set":{"passw":passwo}})
            return render(request,"First/signup.html")