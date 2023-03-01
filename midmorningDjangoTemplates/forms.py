from django import forms


class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField()


class ProductOrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField()
    item = forms.CharField(max_length=50)


class EmployeeLoginForm(forms.Form):
    Employee_name = forms.CharField(max_length=100)
    Employee_email = forms.EmailField(max_length=100)
    password = forms.CharField()
