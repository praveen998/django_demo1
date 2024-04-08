from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def index(request):
    name="praveen"
    return render(request,'index.html',{'name':name})

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
    return render(request,"show.html",{'employees':employees})

def myview(request):
    items=['item1','item2','item3','item4','item5']
    it=['it1','it2','it3']
    return render(request,'myview.html',{'items':items,'it':it})


def edit(request,id):
    employee=Employee.objects.get(eid=id)
    print("#####################")
    print(type(id))
    print("#######################")
    return render(request,'edit.html',{'employee':employee})


def update(request,id):
    print("#####################")
    print(type(id))
    print("#######################")
    
    employee=Employee.objects.get(eid=id)
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/emp/show")
    return render(request,'edit.html',{'employee':employee})

def delete(request,id):
    return HttpResponse('destroy')


