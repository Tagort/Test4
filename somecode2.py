class Dog():
	def __init__(self,dogname,dogcolor,dogheight,dogbuild,dogmood,dogage):
	#здесь мы установим атрибуты для нашего класса «Собака»
		self.name = dogname
		self.color = dogcolor
		self.height = dogheight
		self.build = dogbuild
		self.mood = dogmood
		self.age = dogage
		self.Hungry = False
		self.Tired = False

	def Eat(self):
		if self.Hungry:
			print 'Ммм Ммм...Ням Ням'
			self.Hungry = False
		else:
			print 'Нюх-нюх...Не голоден'	
	def Sleep(self):
		if self.Tired:
			print 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
			self.Tired = False

	def Bark(self):
		if self.mood == 'Сварливый':
			print 'Рррррррр... Гав! Гав!'
		elif self.mood == 'Спокойный':
			print 'Зевает...ok...Гав'
		elif self.mood == 'Сумасшедший':
			print 'Ав Ав Ав Ав Ав Ав Ав Ав Ав Ав Ав Ав'
		else:
			print 'Гав! Гав!'

Beagle = Dog('Арчи','Коричневый','Низкий','Пухлый','Сварливый',12)
print 'Моя кличка %s' % Beagle.name
print 'Мой окрас %s' % Beagle.color
print 'Моё настроение %s' % Beagle.mood
print 'Я голоден = %s' % Beagle.Hungry
Beagle.Eat()
Beagle.Hungry = True
Beagle.Eat()
Beagle.Bark()


