from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Match, Season
from .forms import CreateSeasonForm, MatchForm
from .forms import TeamFormSet

from .ladder import get_ladder_data
from.berger import generate_season


def match_list(request, season_id):
    matches = Match.objects.filter(season=season_id).order_by('round')
    return render(request, 'pong/match_list.html', {
        'matches': matches
    })


def edit_match(request, season_id, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pong/match.html', {'match': form})
    else:
        form = MatchForm(instance=match)
    return render(request, 'pong/match.html', {'match': form})


def ladder_view(request, season_id):

    return render(request, 'pong/ladder.html', {
        'ladder_list': get_ladder_data(season_id)
    })


def season_list(request):
    seasons = Season.objects.all().order_by('-id')
    return render(request, 'pong/season_list.html', {
        'seasons': seasons
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

