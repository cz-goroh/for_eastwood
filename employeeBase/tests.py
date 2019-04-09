import datetime
from django.test import TestCase
from django.test.client import Client
from .models import Department, Employee

class DepartamentTestCase(TestCase):

    # def test_newDepartament(self):
    #     Department.objects.create(name = 'Бездельников')

    def test_newEmployee(self):
        Department.objects.create(name = 'Бездельников')
        Employee.objects.create(
            name = 'Макар',
            surname = 'Макар',
            patronymic = 'Макарович',
            birth_day = datetime.date.today(),
            email = 'mail@mail.com',
            tel = '+71234567890',
            Position = 'Грузчик',
            departament = min(Department.objects.all())
        )

    def test_get_index(self):
        c = Client()
        response = c.get('/employee/')

    def test_get_list(self):
        c = Client()
        response = c.get('/employee/list/')
        response.status_code

    def test_get_alfabet(self):
        c = Client()
        response = c.get('/employee/alfabet/')
        response.status_code

    def test_get_filters_work(self):
        c = Client()
        response = c.get('/employee/list/',{'departament': 2, 'is_work': 'work'} )
        response.status_code

    def test_get_filters_fired(self):
        c = Client()
        response = c.get('/employee/list/',{'departament': 2, 'is_work': 'fired'} )
        response.status_code

    def test_get_letters(self):
        c = Client()
        response = c.get('/employee/alfabet/', {'letters': 2})
        response.status_code


# Create your tests here.
