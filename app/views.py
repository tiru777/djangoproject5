from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from app.models import Employee
from app.forms import EmployeeForm


def home(request):
    return render(request, 'home.html')


def create_employee_post(request):
    form = EmployeeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/list")
    return render(request, 'create_employee.html', context={'form': form})


def list_employee(request):
    data = Employee.objects.all()
    return render(request, 'employee_list.html', {'tiru': data})


def employee_get(request, id):
    data = Employee.objects.get(id=id)
    return render(request, 'detailedlist.html', {'tiru': data})


def update_employee(request, id):
    employee_object = get_object_or_404(Employee,id=id) # Employee.object.get(id=id)
    form = EmployeeForm(instance=employee_object)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    return render(request, 'update.html', context={'form': form})


def employee_delete(request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect("/list")