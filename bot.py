from TelegramBotInterface import telegramapi
import time
from random import randint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('TOKEN', help='Telegram bot token')
parser.add_argument('CHAT_ID', help='Your ChatID')
args = parser.parse_args()

#TOKEN = '1288737573:AAHcOinC_yFxk3q48sCO5EhFhu0W9e-f1Ho'
TOKEN = args.TOKEN
#MY_CHAT_ID = '1003891039'
MY_CHAT_ID = args.CHAT_ID

tb = telegramapi.TelegramAPI(TOKEN)
tb.sendMessage(MY_CHAT_ID, 'Starting bot.')

prevCommand = ''

def checkCommands(command):
	global prevCommand
	if command != prevCommand:
		if command == '/hola':
			tb.sendMessage(MY_CHAT_ID, 'Hola ' + tb.readLastMessage()['fromName'].lower()+'.')
			tb.sendMessage(MY_CHAT_ID, 'Como estas?')
			print(command)
			prevCommand = command
			command = None

		elif command == '/ayuda':
			comm = ''.join(tb.getCommands())
			tb.sendMessage(MY_CHAT_ID, comm)
			print(command)
			prevCommand = command
			command = None

		elif command == '/quiensos':
			tb.sendMessage(MY_CHAT_ID, 'Soy un bot.')
			time.sleep(0.5)
			tb.sendMessage(MY_CHAT_ID, 'Te puedo ayudar en todo lo que necesites.')
			time.sleep(0.75)
			tb.sendMessage(MY_CHAT_ID, 'Pero para vos me tenes que configurar para saber como ayudarte.')
			time.sleep(0.25)
			tb.sendMessage(MY_CHAT_ID, 'Aqui están algunas de mis configuraciones: ')
			time.sleep(0.5)
			tb.sendMessage(MY_CHAT_ID, str(tb.getMe()))
			print(command)
			prevCommand = command
			command = None

		elif command == '/dado':
			tb.sendDice(MY_CHAT_ID)
			print(command)
			prevCommand = command
			command = None

		elif '/numerorandom' in command:
			numsRaw = []
			try:
				raw = command.strip('/numerorandom ')
			except:
				tb.sendMessage(MY_CHAT_ID, 'Debes ingresar 2 numeros')
			min_max = list(map(int, raw.split(',')))
			
			num = randint(min_max[0],min_max[1])
			tb.sendMessage(MY_CHAT_ID, str(num))
			
			prevCommand = command
			command = None

		else:
			tb.sendMessage(MY_CHAT_ID, 'uh ni idea maestro')
			print(command)
			prevCommand = command
			command = None
	else:
		#tb.sendMessage(MY_CHAT_ID, 'desea repetir el ultimo comando?')
		print('los comandos son iguales')
		command = None


while True:
	command = tb.readLastMessage()['message']
	print('El comando es: ' + command)
	checkCommands(command)
	time.sleep(1)
