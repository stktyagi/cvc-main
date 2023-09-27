from django import forms
from .models import Team

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'title', 'description', 'country', 'linkedin', 'image']