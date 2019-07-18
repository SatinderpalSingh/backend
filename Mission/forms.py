from django import forms 
from .models import mission


class MissionForm(forms.ModelForm):

    class Meta:
        model = mission 

        fields = ('Mission',)
