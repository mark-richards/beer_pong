from django import forms
from django.forms import formset_factory


class CreateSeasonForm(forms.Form):
    season = forms.CharField(label='Season Name', max_length=30)


class TeamForm(forms.Form):
    name = forms.CharField(label="Team Name", max_length=30)

TeamFormSet = formset_factory(TeamForm, extra=1)
