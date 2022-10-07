from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_view(request):
    return render(request,"first.html")

def home_view(request):

    about={"name":"nived","number":187,"my_list":["aaama","poocha",1,2,3,4],"html0":"<h1>Heading </h1>"}

    return render(request,"home.html",about)


def pic_view(request):

    return render(request,"pics.html",{})