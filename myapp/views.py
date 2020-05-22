from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
from django.contrib.auth.models import User, auth

from django.http import HttpResponse
from .models import Company
from .models import Employee

from django.core.files.base import ContentFile
from . import pt

def company(request):
    if request.user.is_authenticated:
        obj = Company.objects.all()
        return render(request, 'company.html', {'company':obj})
    else:
        return redirect('/')


def employee(request):
    if request.user.is_authenticated:
        obj = Employee.objects.all()
        return render(request, 'employee.html', {'employee': obj})
    else:
        return redirect('/')

def addemp(request):
    if request.user.is_authenticated:
        return render(request, 'addemp.html')
    else:
        return redirect('/')


def addcom(request):
    if request.user.is_authenticated:
        return render(request, 'addcom.html')
    else:
        return redirect('/')


def index(request):
    if request.method=='POST':
        uname = request.POST['uname']
        pwd = request.POST['passwd']

        user = auth.authenticate(username=uname, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'index.html', {'msg': 'err'})
    else:
        return render(request, 'index.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('/')


def addcprocess(request):
    if request.user.is_authenticated:
        ema = request.POST['email']
        nam = request.POST['nam']
        webs = request.POST['web']

        Company.objects.create(name = nam, email = ema, website = webs)

        return HttpResponse('')
    else:
        return redirect('/')
    

def addeprocess(request):
    if request.user.is_authenticated:
        fna = request.POST['fname']
        lna = request.POST['lname']
        com = request.POST['comp']
        ema = request.POST['email']
        tel = request.POST['tele']


        Employee.objects.create(fname = fna, lname = lna, comp = com, email = ema, tele = tel)

        return HttpResponse('')
    else:
        return redirect('/')
    

def cedit(request):
    if request.user.is_authenticated:
        c = Company()
        c.id = request.GET['Cid']
        c.name = request.GET['Cnam']
        c.email = request.GET['Ema']
        c.website = request.GET['Web']

        return render(request, 'cedit.html', {'company': c})
    else:
        return redirect('/')
    


def editcprocess(request):
    if request.user.is_authenticated:
        nnum = request.POST['nidn']
        nam = request.POST['name']
        ema = request.POST['email']
        web = request.POST['web']

        e_comp = Company.objects.get(id=nnum)

        e_comp.name = nam
        e_comp.email = ema
        e_comp.website = web

        e_comp.save()

        return HttpResponse('')
    else:
        return redirect('/')
    


def delcprocess(request):

    if request.user.is_authenticated:
        nnum = request.POST['nindex']

        d_comp = Company.objects.get(id=nnum)

        d_comp.delete()

        return HttpResponse('')
    else:
        return redirect('/')

    

def eedit(request):
    if request.user.is_authenticated:
        e = Employee()
        e.id = request.GET['Eid']
        e.fname = request.GET['Fnam']
        e.lname = request.GET['Lnam']
        e.comp = request.GET['Com']
        e.email = request.GET['Ema']
        e.tele = request.GET['Tel']

        return render(request, 'eedit.html', {'employee': e})
    else:
        return redirect('/')
    

def editeprocess(request):
    if request.user.is_authenticated:
        enum = request.POST['ein']
        fir = request.POST['fnam']
        las = request.POST['lnam']
        compp = request.POST['comp']
        emaill = request.POST['email']
        telep = request.POST['tele']

        e_emp = Employee.objects.get(id=enum)

        e_emp.fname = fir
        e_emp.lname = las
        e_emp.comp = compp
        e_emp.email = emaill
        e_emp.tele = telep

        e_emp.save()

        return HttpResponse('')
    else:
        return redirect('/')

    
def register(request):
    # user = User.objects.create_user(username="admin@admin.com", password="password")
    # user.save()
    return HttpResponse('')


def deleprocess(request):

    if request.user.is_authenticated:
        enum = request.POST['eindex']

        d_emp = Employee.objects.get(id=enum)

        d_emp.delete()

        return HttpResponse('')
    else:
        return redirect('/')

    


def logout(request):
    auth.logout(request)

    return redirect('/')