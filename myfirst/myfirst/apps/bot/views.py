
from django.shortcuts import render
from .models import Bot
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
import random

def bot(request):
	try:
		bot = Bot.objects.get( id = 1 )
	except:
		raise Http404("Статья не найдена")

	return render(request, 'bot/detail.html', {"hello_world":'hello'})

def Eat(request):
	try:
		bot = Bot.objects.get( id = 1 )
	except:
		raise Http404("Статья не найдена")
	hello_world = ''
	if bot.energy < 20 and bot.satiety < 30:
		hello_world = 'you lose, click return all'
	elif bot.satiety == 100:
		hello_world = "kroll don't wanna Eat"
	elif bot.energy <= 10:
		hello_world = "You need to sleep"	
	elif bot.food < 1:
		hello_world = "your refrigerator is empty. You should go to the shop" 
	elif bot.food >= 1 and bot.energy >= 20 and bot.satiety >= 80:
		bot.food -= 1
		bot.satiety = 100
		bot.energy -= 20
		hello_world = 'your food is ' + str(bot.food)
		if random.randint(1,11) == 10:
			hello_world = "you choked on a bone and you were delivered in a hospital"
			bot.money -= 100
	elif bot.food >= 1 and bot.energy >= 20 and bot.satiety <= 70:
		bot.food -= 1
		bot.satiety += 30
		bot.energy -= 20
		hello_world = "your food is " + str(bot.food)
		if random.randint(1,11) == 10:
			hello_world = "you choked on a bone and you were delivered in a hospital"
			bot.money -= 100
	bot.save()
	return render(request, 'bot/detail.html', {"hello_world":hello_world})

def GoToTheHospital(request):
	try:
		bot = Bot.objects.get( id = 1 )
	except:
		raise Http404("Статья не найдена")
	hello_world = ''
	if bot.energy < 20 and bot.satiety < 30:
		hello_world = "you lose. click 'return all' to play again"
	elif bot.health == 100:
		hello_world = "kroll is healthier than bull"
	elif bot.energy <= 10:
		hello_world = "You need to sleep before going to the hospital"
	elif bot.satiety < 20:
		hello_world = "You need to eat and then go where you want"
	elif bot.money <= 40:
		hello_world = "You don't have enough money to heal. You should go to the work"
	elif bot.health > 40:
		bot.money -= 50
		bot.satiety -= 20
		bot.energy -= 20
		bot.health = 100
		if random.randint(1,11) == 10:
			hello_world = "you got the wrong blood, you have AIDS"
			bot.money -= 50
			bot.health -= 20
	elif bot.health <= 40:
		bot.money -= 50
		bot.satiety -= 20
		bot.energy -= 20
		bot.health += 50
		if random.randint(1,11) == 10:
			hello_world = "you got the wrong blood, you have AIDS"
			bot.money -= 50
			bot.health -= 20
	bot.save()
	return render(request, 'bot/detail.html', {"hello_world":hello_world})

def GoToTheShop(request):
	try:
		bot = Bot.objects.get( id = 1 )
	except:
		raise Http404("Статья не найдена")
	hello_world = ""
	if bot.energy < 20 and bot.satiety < 30:
		hello_world = "you lose. click 'return all' to play again"
	elif bot.food >= 15:
		hello_world = "your refrigerator is full"
	elif bot.energy <= 10:
		hello_world = "You need to sleep before going to the shop"
	elif bot.satiety <= 10:
		hello_world = "You need to eat before going to the shop"
	elif bot.money < 70:
		hello_world = "You don't have enough money"
	elif bot.food >= 10:
		bot.satiety -= 20
		bot.energy -= 20
		bot.food = 15
		bot.money -= 70
	elif bot.food < 10:
		bot.satiety -= 20
		bot.energy -= 20
		bot.food += 5
		bot.money -= 70
		if random.randint(1,8) == 10:
			hello_world = "dogs have stolen your food"
			bot.food -= 3
	bot.save()
	return render(request, 'bot/detail.html', {"hello_world":hello_world})

def GoToTheWork(request):
	try:
		bot = Bot.objects.get( id = 1 )
	except:
		raise Http404("Статья не найдена")
	hello_world = ""
	if bot.energy < 20 and bot.satiety < 30:
		hello_world = "you lose. click 'return all' to play again"
		hello_world_2 = ""
	elif bot.energy <= 20:
		hello_world = "You need to sleep"
	elif bot.satiety <= 20:
		hello_world = "You need to eat"
	elif bot.health == 10:
		hello_world = "you may die at the work"
	else:
		bot.health -= 10
		bot.satiety -= 30
		bot.energy -= 30
		bot.money += 200
		if random.randint(1,8) == 10:
			hello_world = "your salary was delayed"
			bot.money -= 200
	bot.save()
	return render(request, 'bot/detail.html', {"hello_world":hello_world})

def Sleep(request):
	try:
		bot = Bot.objects.get( id = 1 )
	except:
		raise Http404("Статья не найдена")
	hello_world = ""
	if bot.energy < 20 and bot.satiety < 30:
		hello_world = "you lose. click 'return all' to play again"
		hello_world_2 = ""
	elif bot.energy == 100:
		hello_world = "you don't need to sleep"
	elif bot.satiety < 30:
		hello_world = "eat or you will die while you will be sleeping"
	elif bot.energy < 20:
		bot.satiety -= 30
		bot.energy += 80
		bot.energy -= 40
		if random.randint(1,10) == 2:
			hello_world = "insomnia attacked you at night"
			bot.energy -= 40
	elif bot.energy >= 20:
		bot.satiety -= 30
		bot.energy = 100
		if random.randint(1,10) == 2:
			hello_world = "insomnia attacked you at night"
			bot.energy -= 40
	bot.save()
	return render(request, 'bot/detail.html', {"hello_world":hello_world})

def ReturnAll(request):
	try:
		bot = Bot.objects.get( id = 1 )
	except:
		raise Http404("Статья не найдена")
	hello_world = "You returned the game"
	bot.food = 10
	bot.health = 100
	bot.energy = 100
	bot.satiety = 100
	bot.money = 1000
	bot.save()
	return render(request, 'bot/detail.html', {"hello_world":hello_world})