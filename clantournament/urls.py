from django.contrib import admin
from django.urls import path
from .views import clantournamentmain, tournamentdetailfunc, TournamentCreate, TournamentUpdate
urlpatterns = [
    path('', clantournamentmain, name='clantournament'),
    path('detail/<int:pk>', tournamentdetailfunc, name='tournamentdetail'),
    path('create/', TournamentCreate.as_view(), name='tournamentcreate'),
    path('update/<int:pk>', TournamentUpdate.as_view(), name='tournamentupdate')
]