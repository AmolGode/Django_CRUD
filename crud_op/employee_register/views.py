from django.shortcuts import redirect, render

from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request,'employee_register/employee_list.html',context)

def employee_form(request,id=0):
    if request.method == 'GET':
        if id == 0:#GET
            form = EmployeeForm()
        else:#GET Update
            employee = Employee.objects.get(id=id)
            form = EmployeeForm(instance=employee)

        return render(request,'employee_register/employee_form.html',{'form':form})
    else:#POST Save
        if id == 0:
            form = EmployeeForm(request.POST)
        else:#POST Save Update
            employee = Employee.objects.get(id=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
                form.save()
        return redirect('/employee_register/list/')

def employee_delete(request,id):
    employee = Employee(id=id)
    employee.delete()
    return redirect('/employee_register/list/')