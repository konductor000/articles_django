from django.shortcuts import render
from .models import Bot
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def bot(request):
	try:
		bot = Bot.objects.get( id = 1 )
	except:
		raise Http404("Статья не найдена")
	return render(request, 'bot/detail.html', {"hello_world":bot.food})

def make_move(request):
	pass