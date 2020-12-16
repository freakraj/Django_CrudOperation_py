from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee 

# Create your views here.

def employee_list(request):
    # this line for getting the employee model to all data objects to represent employee_list key value pair and storing to context variable 
    context = {'employee_list': Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)

def employee_form(request,id=0):
    if request.method =='GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
            # this line of code for represent form.py file to inside EmployeeForm class to calling and storing form variable  
        return render(request,"employee_register/employee_form.html", {'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
             # this code is EmployeeForm class is  posted form data to save the employee table and redirect to employee_list.html form
            form = EmployeeForm(request.POST,instance=employee)     
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return  redirect('/employee/list')