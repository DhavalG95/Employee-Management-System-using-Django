from django.shortcuts import render ,HttpResponse ,redirect
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    
    return render(request,'index.html')

def all_emp(request):
    emp = Employee.objects.all()
    print(emp)
    return render(request,'view_all_emp.html',context={"emps":emp})

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        salary = request.POST.get("salary")
        bonus = request.POST.get("bonus")
        phone = request.POST.get("phone")
        dept = request.POST.get("dept")
        role = request.POST.get("role")
        Employee.objects.create(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())

        return HttpResponse("Employee added Successfully")

    elif request.method=="GET":
        return render(request,'add_emp.html')

    else:
        return HttpResponse("An Exception Occured! Employee has not been saved")



def remove_emp(request,pk=0):
    if pk:
        try:
            emp_id = Employee.objects.get(id=pk)
            emp_id.delete()
            return redirect('all_emp')
        except:
            return HttpResponse("please enter a valid id")

    emps = Employee.objects.all()

    return render(request,'remove_emp.html',context={"emps":emps})

def filter_emp(request):
    if request.method == "POST":
        name = request.POST.get("first_name")
        dept = request.POST.get("dept")
        role = request.POST.get("role")

        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        if dept:
            emps = emps.filter(dept__name__icontains=dept)

        if role:
            emps = emps.filter(role__name__icontains=role)
        
        return render(request,'view_all_emp.html',context={"emps":emps})

    elif request.method == "GET":
        return render(request,"filter_emp.html")

    else:
        return HttpResponse("An Exception Occured")
        