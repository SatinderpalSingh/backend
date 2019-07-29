from django import forms
from .models import mission, vision

class principal_desk_form(forms.Form):
     principal_img 	= forms.ImageField()
     principal_name     = forms.CharField()
     principal_message 	= forms.CharField(widget=forms.Textarea)

class goal_form(forms.Form):
	long_term_goals = forms.CharField(widget=forms.Textarea)
	short_term_goals = forms.CharField(widget=forms.Textarea)
	
	def __str__(self):
	    return "Goal " + str(datetime.datetime.now())

class MissionForm(forms.ModelForm):
    class Meta:
        model = mission

        fields = ('Mission',)

class VisionForm(forms.ModelForm):

    class Meta:
        model = vision

        fields = ('Vision',)

class history_form(forms.Form):
	History = forms.CharField(widget=forms.Textarea)

class campus_form(forms.Form):
	description	= forms.CharField(widget=forms.Textarea)

class Balance_Sheet_form(forms.Form):
        Name         = forms.CharField()
        Files  	     = forms.FileField()

class get_Gov_files(forms.Form):
	Name_of_File	= forms.CharField()
	File		= forms.FileField()

class get_Finance(forms.Form):
         Name            = forms.CharField()
         Details         = forms.CharField()
         Designation     = forms.CharField()

class Cultural_Committee_form(forms.Form):
     description = forms.CharField(widget=forms.Textarea)

class Cultural_Committee_Achievements_form(forms.Form):
     achievements = forms.CharField(widget=forms.Textarea)

class File_input_form(forms.Form):
     Committee_members	= forms.CharField(max_length = 50)
     designation	= forms.CharField(max_length = 50)

#class Software_Automation_Committee_form(forms.Form):
#     Committee_members	= forms.CharField(max_length = 50)
#     designation	= forms.CharField(max_length = 50)

#class Supporting_Staff_form(forms.Form):
#     Committee_members	= forms.CharField(max_length = 50)
#     designation	= forms.CharField(max_length = 50)

class Roll_of_Honour_form(forms.Form):
     fileName = forms.CharField(label="Name of File")
     file_ROH = forms.FileField(label="File")


