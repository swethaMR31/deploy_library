from django.shortcuts import render
from mysql_app.models import EmployeeDetails
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import EmployeeDetails
from django.views.generic.edit import CreateView
from django.views import View


# Create your views here.

'''def index(request):
    employee_details = EmployeeDetails.objects.all()
    return render(request, "mysql_app/index.html", context = {"details": employee_details})'''
class Myview(View):
    def get(self,request):
        return HttpResponse('Result')
class Employee_create(CreateView):
    model=EmployeeDetails
    fields='__all__'
    success_url = '/list/'

class Employee_list(ListView):
    model=EmployeeDetails

class Employee_Detail(DetailView):
    model=EmployeeDetails

class Employee_Update(UpdateView):
    model=EmployeeDetails
    fields=['first_name','last_name','email']
    success_url = "/list/"

class Employee_Delete(DeleteView):
    model=EmployeeDetails
    success_url = '/list/'

