from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RawInput
from .models import Example

# Create your views here.


def input_values(request):
    my_form = RawInput()    

    if request.method == "POST":
        
        my_form =  RawInput(request.POST)

        if my_form.is_valid():
            print(my_form.cleaned_data)
            Example.objects.create(**my_form.cleaned_data)



    context = {
        "form": my_form
    }

    

    return render(request,"input_values.html",context)
