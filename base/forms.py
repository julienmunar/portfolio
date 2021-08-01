from django import forms
from django.forms import ModelForm
from .models import Project

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'thumbnail','body']

    
    def __init__(self, *args, **kwargs):
        super(AddProjectForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control','placeholder':'Type to title...'})

        self.fields['body'].widget.attrs.update(
               {'class': 'form-control','placeholder':'Type to description...'})


        self.fields['thumbnail'].widget.attrs.update(
            {'class': 'form-control','type':'file','id':'formFile'})


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']