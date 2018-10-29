from django import forms
from django.forms import formset_factory
from .models import Match


class CreateSeasonForm(forms.Form):
    season = forms.CharField(label='Season Name', max_length=30)


class TeamForm(forms.Form):
    name = forms.CharField(label="Team Name", max_length=30)


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ['home_cups_remaining', 'away_cups_remaining']
        exclude = ['round', 'home_team', 'away_team']


TeamFormSet = formset_factory(TeamForm, extra=1)
