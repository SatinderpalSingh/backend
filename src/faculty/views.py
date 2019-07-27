from django.shortcuts import render

# Create your views here.
from .forms import PatentForm

# Create your views here.

def patent(request):
    if request.method =='POST':
        form = PatentForm(request.POST)


        if form.is_valid():
            form.save()
            print("valid")

    form = PatentForm()
    return render(request, 'form.html',{'form':form})
