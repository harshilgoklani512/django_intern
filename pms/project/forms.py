from django import forms
from .models import Project,Projet_team
from user.models import User

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model =Project
        fields ='__all__'
        
    

class ProjectTeamCreationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_developer=True))
    
    class Meta:
        model =Projet_team
        fields ='__all__'