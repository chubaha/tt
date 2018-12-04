from django.contrib import auth
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from empoyees.forms import LoginForm, EditForm, CreateForm
from empoyees.models import Employees
from django.db.models import Q
from django.core import serializers

#вывод дерева сотрудников
def employees(request):
    emp = Employees.objects.all()
    return render(request, 'employees/employees.html', locals())

#вывод списка сотрудников и сортировка без ajax
def all_employees(request):
    if not request.GET.get('sort_param'):
        all_list = Employees.objects.all()
    else:
        all_list = Employees.objects.order_by(request.GET.get('sort_param'))
    return render(request, 'employees/all-list.html', locals())

#поиск сотрудников без ajax
def search_list(request):
    all_list = Employees.objects.filter(Q(name__icontains=request.GET.get('search')) | Q(position__icontains=request.GET.get('search')) | Q(date_begin__icontains=request.GET.get('search')) | Q(salary__icontains=request.GET.get('search')))
    return render(request, 'employees/search.html', locals())

#список сотрудников для сортировки и поиска с помощью ajax
def all_employees_ajax(request):
    all_list = Employees.objects.all()
    return render(request, 'employees/all-list-ajax.html', locals())

#поиск сотрудников с помощью ajax
@csrf_exempt
def search_ajax(request):
    employees = Employees.objects.filter(Q(name__icontains=request.POST.get('request_search')) | Q(position__icontains=request.POST.get('request_search')) | Q(date_begin__icontains=request.POST.get('request_search')) | Q(salary__icontains=request.POST.get('request_search')))
    data = serializers.serialize("json", employees, fields=('name','position', 'date_begin', 'salary'))
    return JsonResponse(data, safe=False)

#поиск сотрудников с помощбю ajax для приватной страницы
@csrf_exempt
def search_ajax_edit(request):
    employees = Employees.objects.filter(Q(name__icontains=request.POST.get('request_search')) | Q(position__icontains=request.POST.get('request_search')) | Q(date_begin__icontains=request.POST.get('request_search')) | Q(salary__icontains=request.POST.get('request_search')))
    data = serializers.serialize("json", employees, fields=('name','position', 'date_begin', 'salary', 'photo'))
    return JsonResponse(data, safe=False)

#сортировка с помощью ajax
def sorter_ajax(request):
    employees = Employees.objects.order_by(request.GET.get('sort'))
    data = serializers.serialize("json", employees, fields=('name','position', 'date_begin', 'salary', 'photo'))
    return JsonResponse(data, safe=False)

#авторизация
def login(request):
    form_auth = LoginForm(request.POST or None)
    if request.method == "POST" and form_auth.is_valid():
        username_auth = request.POST.get('username_auth','')
        password_auth = request.POST.get('password_auth','')
        user = auth.authenticate(username=username_auth, password=password_auth)
        if user is not None:
            auth.login(request, user)
            request.session.set_expiry(43200)
            return redirect("/privat-page/")
    return render(request, 'employees/privat-page.html', locals())

#вывод списка сотрудников для приватной страницы
def privat_page(request):
    form = EditForm(request.POST or None)
    if request.user.is_authenticated:
        if not request.GET.get('sort_param'):
            all_list = Employees.objects.all()
        else:
            all_list = Employees.objects.order_by(request.GET.get('sort_param'))
    return render(request, 'employees/privat-page.html', locals())

#выход из учетной записи
def logout(request):
    auth.logout(request)
    return redirect("/privat-page/")

#удаление сотрудника
def delete(request, id):
    try:
        employee = Employees.objects.get(id=id)
        employee.delete()
        return redirect("/privat-page/")
    except Employees.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого сотрудника не существует</h2>")

#редактирование сотрудника
def edit(request, id):
    instance = get_object_or_404(Employees, id=id)
    form_edit = EditForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == "POST" and form_edit.is_valid():
        new_form = form_edit.save()
        return redirect("/privat-page/")
    return render(request, 'employees/edit-page.html', locals())

#создание сотрудника
def create(request):
    form_create = CreateForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form_create.is_valid():
        new_form = form_create.save()
        return redirect("/privat-page/")
    return render(request, 'employees/create.html', locals())
