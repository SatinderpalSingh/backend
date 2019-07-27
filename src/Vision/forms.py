from django import forms
from .models import vision


class VisionForm(forms.ModelForm):

    class Meta:
        model = vision

        fields = ('Vision',)
