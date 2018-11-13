from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import UpdateView
from .models import Match, Season
from .forms import CreateSeasonForm, MatchForm
from .forms import TeamFormSet

from .ladder import get_ladder_data
from .berger import generate_season


class SeasonList(generic.ListView):
    template_name = 'pong/season_list.html'
    context_object_name = 'seasons'

    def get_queryset(self):
        return Season.objects.all().order_by('-id')


class MatchListView(generic.ListView):
    context_object_name = 'matches'
    template_name = 'pong/match_list.html'

    def get_queryset(self):
        return Match.objects.filter(season__pk=self.kwargs["season_pk"]).order_by('round')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['season'] = Season.objects.get(pk=self.kwargs["season_pk"])
        return context


class MatchUpdate(UpdateView):
    model = Match
    template_name = 'pong/match.html'
    form_class = MatchForm


def ladder_view(request, season_id):

    return render(request, 'pong/ladder.html', {
        'ladder_list': get_ladder_data(season_id),
        'season': Season.objects.get(pk=season_id)
    })

def create_season_view(request):
    if request.method == 'POST':
        create_season_form = CreateSeasonForm(request.POST)
        team_formset = TeamFormSet(request.POST)
        if create_season_form.is_valid() and team_formset.is_valid():
            season = create_season_form.data['season']
            teams = []
            for team_form in team_formset:
                name = team_form.cleaned_data['name']
                teams.append(name)
            season_id = generate_season(season, teams)
            return HttpResponseRedirect('/{}/fixture'.format(season_id))
    else:
        create_season_form = CreateSeasonForm()
        team_formset = TeamFormSet()

    context = {
        'create_season_form': create_season_form,
        'team_formset': team_formset,
    }
    return render(request, 'pong/create_season.html', context)

