from django.db import models 
from django.db.models import Model 
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

	'''def Eat(self):
		mess = ""
		mess_2 = "your satiety now is"
		if self.energy < 20 and self.satiety < 30:
			mess = "you lose. click 'return all' to play again"
			mess_2 = ""
			data.append(mess)
		elif self.satiety == 100:
			mess = "kroll don't wanna Eat"
			data.append(mess)
		elif self.energy <= 10:
			mess = "You need to sleep"
			data.append(mess)
		elif self.food < 1:
			mess = "your refrigerator is empty. You should go to the shop" 
			data.append(mess)
		elif self.food >= 1 and self.energy >= 20 and self.satiety >= 80:
			b.self.food -= 1
			b.self.satiety = 100
			b.self.energy -= 20
			if random.randint(1,11) == 10:
				mess = "you choked on a bone and you were delivered in a hospital"
				b.self.money -= 100
				data.append(mess)
		elif self.food >= 1 and self.energy >= 20 and self.satiety <= 70:
			b.self.food -= 1
			b.self.satiety += 30
			b.self.energy -= 20
			if random.randint(1,11) == 10:
				mess = "you choked on a bone and you were delivered in a hospital"
				b.self.money -= 100
				data.append(mess)
		return '{} {}. {}'.format(mess_2, self.satiety, mess)

	def GoToTheHospital(self):
		mess = ""
		if self.energy < 20 and self.satiety < 30:
			mess = "you lose. click 'return all' to play again"
			mess_2 = ""
			data.append(mess)
		elif self.health == 100:
			mess = "kroll is healthier than bull"
			data.append(mess)
		elif self.energy <= 10:
			mess = "You need to sleep before going to the hospital"
			data.append(mess)
		elif self.satiety < 20:
			mess = "You need to eat and then go where you want"
			data.append(mess)
		elif self.money <= 40:
			mess = "You don't have enough money to heal. You should go to the work"
			data.append(mess)
		elif self.health > 40:
			b.self.money -= 50
			b.self.satiety -= 20
			b.self.energy -= 20
			b.self.health = 100
			if random.randint(1,11) == 10:
				mess = "you got the wrong blood, you have AIDS"
				b.self.money -= 50
				b.self.health -= 20
				data.append(mess)
		elif self.health <= 40:
			b.self.money -= 50
			b.self.satiety -= 20
			b.self.energy -= 20
			b.self.health += 50
			if random.randint(1,11) == 10:
				mess = "you got the wrong blood, you have AIDS"
				b.self.money -= 50
				b.self.health -= 20
				data.append(mess)
		return "your health is {} points. {}".format(self.health, mess)

	def GoToTheShop(self):
		mess = ""
		if self.energy < 20 and self.satiety < 30:
			mess = "you lose. click 'return all' to play again"
			mess_2 = ""
			data.append(mess)
		elif len(self.items) < 3:
			if self.food >= 15:
				mess = "your refrigerator is full"
				data.append(mess)
			elif self.energy <= 10:
				mess = "You need to sleep before going to the shop"
				data.append(mess)
			elif self.satiety <= 10:
				mess = "You need to eat before going to the shop"
				data.append(mess)
			elif self.money < 70:
				mess = "You don't have enough money"
				data.append(mess)
			elif self.food >= 10:
				b.self.satiety -= 20
				b.self.energy -= 20
				b.self.food = 15
				b.self.money -= 70
			elif self.food < 10:
				b.self.satiety -= 20
				b.self.energy -= 20
				b.self.food += 5
				b.self.money -= 70
				if random.randint(1,11) == 10:
					mess = "dogs have stolen your food"
					b.self.food -= 3
					data.append(mess)
		else:
			if self.food >= 15:
				mess = "your refrigerator is full"
				data.append(mess)
			elif self.energy <= 10:
				mess = "You need to sleep before going to the shop"
				data.append(mess)
			elif self.satiety <= 10:
				mess = "You need to eat before going to the shop"
				data.append(mess)
			elif self.money < 80:
				mess = "You don't have enough money"
				data.append(mess)
			elif self.food >= 8:
				b.self.satiety -= 20
				b.self.energy -= 20
				b.self.food = 15
				b.self.money -= 80
			elif self.food < 8:
				b.self.satiety -= 20
				b.self.energy -= 20
				b.self.food += 7
				b.self.money -= 80
		return "you have {} carrots. {}".format(self.food, mess)

	def GoToTheWork(self):
		mess = ""
		if self.energy < 20 and self.satiety < 30:
			mess = "you lose. click 'return all' to play again"
			mess_2 = ""
			data.append(mess)
		elif self.energy <= 20:
			mess = "You need to sleep"
			data.append(mess)
		elif self.satiety <= 20:
			mess = "You need to eat"
			data.append(mess)
		elif self.health == 10:
			mess = "you may die at the work"
			data.append(mess)
		else:
			b.self.health -= 10
			b.self.satiety -= 30
			b.self.energy -= 30
			b.self.money += 200
			if random.randint(1,11) == 10:
				mess = "your salary was delayed"
				b.self.money -= 200
				data.append(mess)
		return "you have {} money. {}".format(self.money, mess)

	def Sleep(self):
		mess = ""
		if self.energy < 20 and self.satiety < 30:
			mess = "you lose. click 'return all' to play again"
			mess_2 = ""
			data.append(mess)
		elif self.energy == 100:
			mess = "you don't need to sleep"
			data.append(mess)
		elif self.satiety < 30:
			mess = "eat or you will die while you will be sleeping"
			data.append(mess)
		elif self.energy < 20:
			b.self.satiety -= 30
			b.self.energy += 80
			if len(self.items) >= 2:
				if random.randint(1,15) == 2:
					mess = "insomnia attacked you at night"
					b.self.energy -= 40
					data.append(mess)
			else:
				if random.randint(1,7) == 2:
					mess = "insomnia attacked you at night"
					data.append(mess)
					b.self.energy -= 40
		elif self.energy >= 20:
			b.self.satiety -= 30
			b.self.energy = 100
			if len(self.items) >= 2:
				if random.randint(1,15) == 2:
					mess = "insomnia attacked you at night"
					b.self.energy -= 40
					data.append(mess)
			else:
				if random.randint(1,7) == 2:
					mess = "insomnia attacked you at night"
					b.self.energy -= 40
					data.append(mess)
		return "you have {} energy. {}".format(self.energy, mess)

	def BuyTheProperty(self):
		mess = ""
		if self.energy < 20 and self.satiety < 30:
			mess = "you lose. click 'return all' to play again"
			mess_2 = ""
		elif len(self.items) == 1:
			if self.money < 2000:
				mess = "You don't have enough money to buy a mattress. "
			elif self.money >= 2000:
				b.self.items.append("mattress")
				b.self.money -= 2000
				mess = "you have successfully bought a mattress. "
		elif len(self.items) == 2:
			if self.money < 2500:
				mess = "You don't have enough money to buy a bike. "
			elif self.money >= 2500:
				b.self.items.append("bike")
				b.self.money -= 2500
				mess = "you have successfully bought a bike. "
		return "{}you have it {}.".format(mess, self.items)

'''





