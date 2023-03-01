from django.shortcuts import render
from .forms import UserRegistrationForm
from .forms import ProductOrderForm
from .forms import EmployeeLoginForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog_list(request):
    return render(request, 'blog_list.html')


def contact(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def register(request):
    submit_button = request.POST.get("btn-reg")
    name = ''
    email = ''
    password = ''
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
    context = {'form': form, 'submit_button': submit_button,
               'name': name, 'email': email, 'password': password}
    return render(request, 'register.html', context)


def product_order(request):
    submit = request.POST.get("btn-order")
    name = ''
    email = ''
    password = ''
    item = ''
    form = ProductOrderForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        item = form.cleaned_data.get('item')
    context = {'form': form, 'submit': submit, 'name': name,
               'email': email, 'password': password, 'item': item}
    return render(request, 'product.html', context)


def employee_login(request):
    submit_button = request.POST.get("btn-login")
    employee_name = ''
    employee_email = ''
    password = ''
    form = EmployeeLoginForm(request.POST or None)
    if form.is_valid():
        employee_name = form.cleaned_data.get('Employee_name')
        employee_email = form.cleaned_data.get('Employee_email')
        password = form.cleaned_data.get('password')
    context = {'form': form, 'submit_button': submit_button,
               'User_name': employee_name, 'User_email': employee_email, 'password': password}
    return render(request, 'employee_information.html', context)
