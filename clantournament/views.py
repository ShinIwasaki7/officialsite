from django.shortcuts import render, redirect, get_object_or_404
from .models import TournamentArticleModel
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def clantournamentmain(request):
  holded_list = TournamentArticleModel.objects.filter(hold_flag='True') #開催された大会
  willhold_list = TournamentArticleModel.objects.filter(hold_flag='False') #開催されていない大会
  return render(request, 'clantournamentapp/tournamentmain.html', {'holded': holded_list, 'willhold': willhold_list})

def tournamentdetailfunc(request, pk):
  object_ = get_object_or_404(TournamentArticleModel, pk=pk)
  return render(request, 'clantournamentapp/tournamentdetail.html', {'object': object_})

class TournamentCreate(CreateView):
  template_name = 'clantournamentapp/create.html'
  model = TournamentArticleModel
  fields = ('title', 'context', 'participants_num', 'date')
  success_url = reverse_lazy('clantournament')

class TournamentUpdate(UpdateView):
  template_name = 'clantournamentapp/update.html'
  model = TournamentArticleModel
  fields = ('title', 'context', 'participants_num', 'date')
  success_url = reverse_lazy('clantournament')

