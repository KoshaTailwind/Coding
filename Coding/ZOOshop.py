class Pet:
	def __init__(self, name, species, age, sex):
		self.__name = name
		self.__species = species
		self.__age = age
		self.__sex = sex
	
	def get_info(self):
		return f'Имя питомца: {self.__name}. Вид: {self.__species}. Пол: {self.__sex}. Возраст: {self.__age}.'
		
class Dog(Pet):
	def __init__(self, name, age, sex, breed):
		super().__init__(name, 'Собака', age, sex)
		self.__breed = breed
		
	def bark(self):
		print('Гав!')
		
	def get_info(self):
		base_info = super().get_info()
		return f'{base_info}, Порода: {self.__breed}'

class Cat(Pet):
	def __init__(self, name, age, sex, color):
		super().__init__(name, 'Кошка', age, sex)
		self.__color = color
		
	def meow(self):
		print('Мяу!')
		
	def get_info(self):
		base_info = super().get_info()
		return f'{base_info}, Порода: {self.__color}'
		
		
#создаю примеры

dog = Dog('Жозефина', 5, 'Девочка', 'Французский бульдог')
cat = Cat('Василий', 4, 'Мальчик', 'Тигровый')

print(dog.get_info())
dog.bark()

print(cat.get_info())
cat.meow()
		
