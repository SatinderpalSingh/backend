# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .forms import MissionForm, VisionForm


def mission(request):
    if request.method =='POST':
        form = MissionForm(request.POST)


        if form.is_valid():
            form.save()
            print("valid")

    form = MissionForm()
    return render(request, 'form.html',{'form':form})


def vision(request):
    if request.method =='POST':
        form = VisionForm(request.POST)


        if form.is_valid():
            form.save()
            print("valid")

    form = VisionForm()


    return render(request, 'form.html',{'form':form})
