from django import forms
from .models import mission, vision


class MissionForm(forms.ModelForm):

    class Meta:
        model = mission

        fields = ('Mission',)

class VisionForm(forms.ModelForm):

    class Meta:
        model = vision

        fields = ('Vision',)
