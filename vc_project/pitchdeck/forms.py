from django import forms
from .models import PitchDeck


class UploadFileForm(forms.Form):

    class Meta:
        model = PitchDeck
        fields = ['name', 'company_name','Sector','Location','PMV','Raising','Email','Assurance', 'Stage']