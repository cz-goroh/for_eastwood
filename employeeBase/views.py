from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.db.models.functions import Substr, Upper
from .models import Department, Employee

# Create your views here.
def letters(self):

    letters =list([f['fl'] for f in Employee.objects.annotate(fl=Upper(Substr('surname', 1, 1))).values('fl')])
    k,m = divmod(len(letters),7)
    letgroups = tuple((letters[i * k + min(i, m):(i + 1) * k + min(i + 1, m)]  for i in range(7)))
    str_for_links = { id:min(val) + '-' + max(val) for id, val in  enumerate(letgroups) if val}
    return {
            'letgroups':letgroups,
            'letters':letters,
            'str_for_links': str_for_links
      }

class EmployeeList(ListView):
    model = Employee
    paginate_by = 2
    #
    def get_queryset(self,  **kwargs):
        try:
            by_departament = Employee.objects.filter(departament = self.request.GET['departament'])
            if self.request.GET['is_work'] == 'work':
                return by_departament.filter(end_work = None)
            else:
                return by_departament.exclude(end_work = None)
            return Employee.objects.filter(departament = self.request.GET['departament']).filter()
        except KeyError:
            return Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EmployeeList, self).get_context_data(**kwargs)
        context['departaments'] = Department.objects.all()
        return context

class EmployeeDetail(DetailView):
    model = Employee

class EmployeeAlfabet(ListView):
    model = Employee
    template_name = 'employeeBase/employee_alfabet.html'
    def  get_queryset(self,  **kwargs):
        # группы букв
        letgroups = letters(self)

        try:
            get_letters = self.request.GET['letters']
            return Employee.objects.annotate(fl=Upper(Substr('surname', 1, 1))).filter(fl__in = letgroups['letgroups'][int(self.request.GET['letters'])])
        except KeyError:
            return Employee.objects.annotate(fl=Upper(Substr('surname', 1, 1))).filter(fl__in = letgroups['letgroups'][0])

    def get_context_data(self, **kwargs):
        context = super(EmployeeAlfabet, self).get_context_data(**kwargs)
        letgroups = letters(self)
        context['str_for_links'] =letgroups['str_for_links']
        return context

def index(request):
    q = {}
    return render(request, 'employeeBase/index.html', context = q)
