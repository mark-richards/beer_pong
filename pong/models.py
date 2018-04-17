from django.db import models
from django.utils import timezone


class Match(models.Model):
    season = models.ForeignKey('Season', on_delete="CASCADE")
    round = models.IntegerField()
    home_team = models.ForeignKey('Team', on_delete="CASCADE", related_name='home_team')
    away_team = models.ForeignKey('Team', on_delete="CASCADE", related_name='away_team')
    home_cups_remaining = models.IntegerField(null=True, blank=True)
    away_cups_remaining = models.IntegerField(null=True, blank=True)

    def __str__(self):
            return '%s Round %s: %s v %s' % (self.season, self.round, self.home_team, self.away_team)


class Team(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
