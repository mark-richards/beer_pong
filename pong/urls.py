from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.season_list, name='season_list'),
    url(r'^(?P<season_id>\d+)/fixture$', views.match_list, name='match_list'),
    url(r'^(?P<season_id>\d+)/ladder$', views.ladder_view, name='ladder_view'),
    url(r'^create-season$', views.create_season_view, name='create_season_view'),
]
