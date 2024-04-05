from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def index(request):
    return HttpResponse('welcome employee')


def emp(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/emp/show')
    else:
        form=EmployeeForm()
    return render(request,'employee_form.html',{'form':form})


def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'name':'praveen'})

def myview(request):
    items=['item1','item2','item3','item4','item5']
    it=['it1','it2','it3']
    return render(request,'myview.html',{'items':items,'it':it})