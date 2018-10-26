from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SeasonList.as_view(), name='season_list'),
    url(r'^(?P<season_pk>\d+)/fixture$', views.MatchListView.as_view(), name='match_list'),
    url(r'^(?P<season_id>\d+)/ladder$', views.ladder_view, name='ladder_view'),
    url(r'^(?P<season_id>\d+)/(?P<pk>\d+)', views.MatchUpdate.as_view(), name='match_edit'),
    url(r'^create-season$', views.create_season_view, name='create_season_view'),
]
