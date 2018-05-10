from django import forms
from django.forms import ModelForm, SelectMultiple, TextInput, Textarea
from .models import Project, ActivityJournal
from django.contrib.auth.models import User


class TimeSelectMultiple(SelectMultiple):
    template_name = 'forms/timeselect.html'



class ProjectForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=TimeSelectMultiple)

    class Meta:
        model = Project
        fields = ['name', 'user', 'description']
  