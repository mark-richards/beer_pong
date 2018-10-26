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
    model = Season
    context_object_name = 'matches'
    template_name = 'pong/match_list.html'

    def get_queryset(self):
        return Match.objects.filter(season__pk=self.kwargs["season_pk"]).order_by('round')


def ladder_view(request, season_id):

    return render(request, 'pong/ladder.html', {
        'ladder_list': get_ladder_data(season_id)
    })


class MatchUpdate(UpdateView):
    model = Match
    template_name = 'pong/match.html'
    fields = ['round', 'home_team', 'away_team', 'home_cups_remaining', 'away_cups_remaining']


# def edit_match(request, season_id, match_id):
#     match = get_object_or_404(Match, pk=match_id)
#     if request.method == "POST":
#         form = MatchForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('pong/match.html', {'match': form})
#     else:
#         form = MatchForm(instance=match)
#     return render(request, 'pong/match.html', {'match': form})


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

