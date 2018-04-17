from django import forms


class CreateSeasonForm(forms.Form):
    season = forms.CharField(label='Season Name', max_length=30)


class TeamForm(forms.Form):
    name = forms.CharField(label="Team Name", max_length=30)
