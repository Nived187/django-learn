from django.shortcuts import render,get_object_or_404
from .models import CarModels
from .forms import CarForm
from django.http import Http404

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


def dynamic_routing(request,my_id):

    #item = CarModels.objects.get(id=my_id)
    #item = get_object_or_404(CarModels,id = my_id)
    
    try:
        item = CarModels.objects.get(id = my_id)

    except  CarModels.DoesNotExist:
        raise Http404


    context = { 
        "item" : item
    }

    return render(request,"dynamic_routing.html",context)




def dynamic_linking(request):

    obj = CarModels.objects.all()
    context = {
        "objects" : obj
    }

    return render(request,"dynamic_linking.html",context)

