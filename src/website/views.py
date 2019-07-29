# Create your views here.
from django.db.models import Max
from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
from .forms import *
from django.views import View
from django.db import connection
from itertools import chain

def front_page(request):
	return render(request, "first_page.html")

def get_principal_desk(request):
	form = principal_desk_form(request.POST, request.FILES or None)
	if form.is_valid():
		obj = principal_desk.objects.create(**form.cleaned_data)
		obj.save()

	context	= {
			"form":form,
		}
	return render(request, "get_pd.html", context)	


def get_mission(request):
    if request.method =='POST':
        form = MissionForm(request.POST)

        if form.is_valid():
            form.save()
            print("valid")

    form = MissionForm()
    return render(request, 'mission_form.html',{'form':form})


def get_vision(request):
    if request.method =='POST':
        form = VisionForm(request.POST)


        if form.is_valid():
            form.save()
            print("valid")

    form = VisionForm()
    return render(request, 'vision_form.html',{'form':form})

def get_goals(request):
	form = goal_form(request.POST or None)
	
	if form.is_valid():
		obj = goal.objects.create(**form.cleaned_data)
		obj.save()

	context = {
			"form":form,
		}

	return render(request, 'goals_form.html', context)

def get_history(request):
	form = history_form(request.POST or None)
	
	if form.is_valid():
		obj = history.objects.create(**form.cleaned_data)
		obj.save()
	
	context = {
			"form":form,
		}

	return render(request, 'history_form.html', context)

def get_campus(request):
	form = campus_form(request.POST or None)

	if form.is_valid():
		obj = campus.objects.create(**form.cleaned_data)
		obj.save()

	context = {
			"form":form,
		}
	
	return render(request, 'campus_form.html', context)

def get_bsheets(request):
	form = Balance_Sheet_form(request.POST, request.FILES or None)

	if form.is_valid():
		obj = Balance_Sheet.objects.create(**form.cleaned_data)
		obj.save()

	context = {
			"form":form,
		}
	
	return render(request, 'bsheets_form.html', context)

 
# stat_bog
# stat_adm_council
# stat_finance_committe
# stat_bos
# non_stat

def get_stat_bog(request):
	obj1 = gov_type_table.objects.get(id = 1) 
	obj = governence_files()
	form = get_Gov_files(request.POST, request.FILES or None)
	
	if form.is_valid():
		obj.type_id_id 	 = obj1.type_id
		obj.Name_of_file = form.cleaned_data.get('Name_of_File')
		obj.files 	 = form.cleaned_data.get('File')
		obj.save()

	context = {
			"form": form,
		}
	form = get_Gov_files()
	return render(request, 'get_stat_bog.html', context)

def get_stat_AC(request):
	obj1 = gov_type_table.objects.get(id = 2) 
	obj = governence_files()
	form = get_Gov_files(request.POST, request.FILES or None)
	
	if form.is_valid():
		obj.type_id_id 	 = obj1.type_id
		obj.Name_of_file = form.cleaned_data.get('Name_of_File')
		obj.files 	 = form.cleaned_data.get('File')
		obj.save()

	context = {
			"form": form,
		}
	form = get_Gov_files()
	return render(request, 'get_stat_AC.html', context)

def get_stat_BOS(request):
	obj1 = gov_type_table.objects.get(id = 4) 
	obj = governence_files()
	form = get_Gov_files(request.POST, request.FILES or None)
	
	if form.is_valid():
		obj.type_id_id 	 = obj1.type_id
		obj.Name_of_file = form.cleaned_data.get('Name_of_File')
		obj.files 	 = form.cleaned_data.get('File')
		obj.save()

	context = {
			"form": form,
		}
	form = get_Gov_files()
	return render(request, 'get_stat_bos.html', context)


def get_non_stat(request):
	obj1 = gov_type_table.objects.get(id = 5) 
	obj = governence_files()
	form = get_Gov_files(request.POST, request.FILES or None)
	
	if form.is_valid():
		obj.type_id_id 	 = obj1.type_id
		obj.Name_of_file = form.cleaned_data.get('Name_of_File')
		obj.files 	 = form.cleaned_data.get('File')
		obj.save()

	context = {
			"form": form,
		}
	form = get_Gov_files()
	return render(request, 'get_non_stat.html', context)

def get_Finance_Committe(request):
	form = get_Finance(request.POST or None)
	if form.is_valid():
		obj = Finance_Committe.objects.create(**form.cleaned_data)
		obj.save()

	context	= {
			"form":form,
		}
	return render(request, "get_stat_FC.html", context)	
	
def Cultural_Committee_page(request):
	form = Cultural_Committee_form(request.POST or None)

	if form.is_valid():
		obj = Cultural_Committee.objects.create(**form.cleaned_data)
		obj.save()
	
	context = {
			"form":form,
		}
	return render(request, "Cultural_Committee_input_form.html", context)

def Cultural_Committee_Achievements_page(request):
	form = Cultural_Committee_Achievements_form(request.POST or None)

	if form.is_valid():
		obj = Cultural_Committee_Achievements.objects.create(**form.cleaned_data)
		obj.save()
	
	form = Cultural_Committee_Achievements_form(request.POST or None)

	context = {
			"form":form,
		}

	return render(request, "Cultural_Committee_Achievements_input_form.html", context)

def Members_of_Examination_Branch_get_page(request):
	form = Input_form(request.POST or None)

	if form.is_valid():
		obj = Members_of_Examination_Branch.objects.create(**form.cleaned_data)
		obj.save()
	
	
	context = {
			"form":form,
		}

	return render(request, "Members_of_Examination_Branch_input_form.html", context)

def Software_Automation_Committee_get_page(request):
	form = Input_form(request.POST or None)

	if form.is_valid():
		obj = Software_Automation_Committee.objects.create(**form.cleaned_data)
		obj.save()
		
	context = {
			"form":form,
		}

	return render(request, "Software_Automation_Committee_input_form.html", context)

def Supporting_Staff_get_page(request):
	form = Input_form(request.POST or None)

	if form.is_valid():
		obj = Supporting_Staff.objects.create(**form.cleaned_data)
		obj.save()
		
	context = {
			"form":form,
		}

	return render(request, "Supporting_Staff_input_form.html", context)

def Roll_of_Honour_get_page(request):
	form = Roll_of_Honour_form(request.POST,request.FILES or None)

	if form.is_valid():
		obj = Roll_of_Honour.objects.create(**form.cleaned_data)
		obj.save()
		
	context = {
			"form":form,
		}

	return render(request, "Roll_of_Honour_input_form.html", context)

#def base_fet(request):
#	obj = principal_desk.objects.get(id=1)
#	return render(request, "principal_desk.html", {"obj":obj}) 


def frontend_views(request, pgid):
	if(pgid == 1):	
		template = "principal_desk.html"
		obj      = principal_desk.objects.get(id=1)


	elif(pgid == 3):
		template = "mission.html"
		obj      = mission.objects.get(id=1)

	elif(pgid == 4):
		template = "vision.html"
		obj	 = vision.objects.get(id = 1)

	elif(pgid == 5):
		template = "goals.html"
		obj	 = goal.objects.get(id = 1)

	elif(pgid == 6):
		template = "history.html"
		obj	 = history.objects.get(id = 1)
	
	elif(pgid == 7):
		template = "campus.html"
		obj	 = campus.objects.get(id = 1)
	
	elif(pgid == 10):
		template = "finance_committee.html"
		obj	 = Finance_Committe.objects.all()

	elif(pgid == 13):
		template = "bsheets.html"
		obj	 = Balance_Sheet.objects.all()
	else:
		
		if(pgid == 8): 
			i=5
		elif(pgid == 9): 
			i=1	
		elif(pgid == 11): 
			i=2
		elif(pgid == 12): 
			i=4		
		template	 = "governence.html"

		obj1 = gov_type_table.objects.filter(type_id = i) 
		obj2 = governence_files.objects.filter(type_id=i)
		obj = list(chain(obj1, obj2))
	return render(request, template, { "obj":obj, } )







