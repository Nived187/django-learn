from django.shortcuts import render
from .models import ComplaintsM
from .forms import ComplaintsF
# Create your views here.

def complain_register(request):

    complaint = ComplaintsF(request.POST)
    
    if complaint.is_valid():
        
        ComplaintsM.objects.create(**complaint.cleaned_data)
    
    context = {
        'complaints':complaint
    }


    return render(request,'complaint.html',context)