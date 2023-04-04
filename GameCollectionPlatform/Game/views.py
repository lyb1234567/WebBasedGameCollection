from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from Game.models import GameModel
from Game.forms import GameForm
# Create your views here.
class GameCreateView(generic.CreateView):
    model = GameModel
    form_class = GameForm
    template_name = 'Game/game_create.html'

    def form_valid(self, form):
        game = form.save(commit=False)
        game.save()
        return HttpResponseRedirect(reverse('Game:game_list'))
