from django.db import models 
import sys
import config
import random
import sqlite3

class Bot(models.Model):
	food = models.IntegerField(default = 10)
	health = models.IntegerField(default = 100)
	energy = models.IntegerField(default = 100)
	satiety = models.IntegerField(default = 100)
	money = models.IntegerField(default = 1000)
	#b = Bot.objects.get(id=1)

	






