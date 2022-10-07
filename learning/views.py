from django.shortcuts import render
from .models import Phone
from learning.forms import create_form

# Create your views here.

def view1(request):

    object1=Phone.objects.get(id=2)

    content={"obj":object1}

    return render(request,"learning_templates/1.html",content)


def phone_create_view(request):

    phone_form=create_form()

    content={"obj":phone_form}

    render(request,"learning_templates/phone_create_form.html",content)

def project_view(request):
    

    return render(request,"navigator.html",{})
