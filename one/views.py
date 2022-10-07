from django.shortcuts import render
from .models import CarModels
from .forms import CarForm

# Create your views here.


def showroom_view(request):

    my_form = CarForm()

    if request.method == 'POST':

        my_form = CarForm(request.POST)

        if my_form.is_valid():

            CarModels.objects.create(**my_form.cleaned_data)
            my_form = CarForm()

    context = {
            'form':my_form
        }
    return render(request,"showroom_view.html",context)

