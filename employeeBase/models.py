from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField('Отдел', max_length = 20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

class Employee(models.Model):
    name = models.CharField('Имя', max_length = 20)
    surname = models.CharField('Фамилия', max_length = 20)
    patronymic = models.CharField('Отчество', max_length = 20)
    birth_day = models.DateField()
    email = models.EmailField()
    tel = models.CharField('Телефон', max_length = 20)
    begin_work = models.DateField(auto_now_add=True)
    end_work = models.DateField(null = True, blank = True)
    Position =  models.CharField('Должность', max_length = 30)
    departament = models.ForeignKey(Department, on_delete = models.CASCADE, verbose_name = 'Отдел')

    def __str__(self):
        return self.patronymic

    def __str__(self):
        return self.name

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
