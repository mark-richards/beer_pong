from django import forms
from django.forms import formset_factory
from .models import Match


class CreateSeasonForm(forms.Form):
    season = forms.CharField(label='Season Name', max_length=30)


class TeamForm(forms.Form):
    name = forms.CharField(label="Team Name", max_length=30)


class MatchForm(forms.ModelForm):

    def __init__(self, *args, disabled_field=True, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        self.fields['round'].disabled = disabled_field
        self.fields['home_team'].disabled = disabled_field
        self.fields['away_team'].disabled = disabled_field


    class Meta:
        model = Match
        fields = ['round', 'home_team', 'away_team', 'home_cups_remaining', 'away_cups_remaining']


TeamFormSet = formset_factory(TeamForm, extra=1)
