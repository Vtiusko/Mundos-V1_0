'''
Faça um prpgrama em python que abra e reproduza o áudio de um arquivo MP3.
'''
from pygame import mixer
from time import sleep

mixer.init()
mixer.music.load('Mundo1\ex021.mp3')
mixer.music.play(-1)

i= 0

while (mixer.music.get_busy()):
	sleep(1)
	if i > 5:
		mixer.music.stop()