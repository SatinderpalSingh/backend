from django import forms
from .models import patent

class PatentForm(forms.ModelForm):
    class Meta:
        model = patent

        fields = ('Department','Obt_fil','Patent_title','Patent_application_no','Patent_grant_year','Commercialized','Licence_fee','Technology_transferred','Organisation_name','Application_date','Application_no')
