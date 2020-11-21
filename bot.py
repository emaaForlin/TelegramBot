from TelegramBotInterface import telegramapi
import time
from random import randint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('TOKEN', help='Telegram bot token')
parser.add_argument('CHAT_ID', help='Your ChatID')
parser.add_argument('RUN_TEST', help='true for run test, else false')
args = parser.parse_args()


TOKEN = args.TOKEN

MY_CHAT_ID = args.CHAT_ID

tb = telegramapi.TelegramAPI(TOKEN)
tb.sendMessage(MY_CHAT_ID, 'Starting bot.')

prevCommand = ''

def run_test():
    tb.sendMessage(MY_CHAT_ID, 'Starting test mode...')
    tb.Update()
    tb.readLastMessage()
    tb.getMe()
    tb.sendMessage(MY_CHAT_ID, str(randint(-65536,65536)))
    tb.sendDice(MY_CHAT_ID)
    tb.sendMessage(MY_CHAT_ID, 'Succefully test. Shutting down...')
    exit()

def shutdown():
	tb.sendMessage(MY_CHAT_ID, 'Are you sure of this? (y,N) You have 4 seconds to choose')
	time.sleep(4)
	if tb.readLastMessage()['message'].lower() == 'y':
		tb.sendMessage(MY_CHAT_ID, "In (10) second i'll be shutted down.")
		time.sleep(10)
		exit()
	else:
		tb.sendMessage(MY_CHAT_ID, "Okey okey, it's a great idea.")
    
def checkCommands(command):
	global prevCommand
	if command != prevCommand:
		if command == '/hi':
			tb.sendMessage(MY_CHAT_ID, 'Hi ' + tb.readLastMessage()['fromName'].lower()+'.')
			tb.sendMessage(MY_CHAT_ID, 'How are you?')
			print(command)
			prevCommand = command
			command = None

		elif command == '/help':
			comm = ''.join(tb.getCommands())
			tb.sendMessage(MY_CHAT_ID, comm)
			print(command)
			prevCommand = command
			command = None

		elif command == '/whoareyou':
			tb.sendMessage(MY_CHAT_ID, "I'm a fucking bot")
			time.sleep(0.5)
			tb.sendMessage(MY_CHAT_ID, 'I can help you on all that you need')
			time.sleep(0.75)
			tb.sendMessage(MY_CHAT_ID, 'But you need to make this shit work')
			time.sleep(0.25)
			tb.sendMessage(MY_CHAT_ID, 'Here is some of my configs.')
			time.sleep(0.5)
			tb.sendMessage(MY_CHAT_ID, str(tb.getMe()))
			print(command)
			prevCommand = command
			command = None

		elif command == '/dice':
			tb.sendDice(MY_CHAT_ID)
			print(command)
			prevCommand = command
			command = None

		elif '/numrand' in command:
			numsRaw = []
			try:
				raw = command.strip('/numrand ')
			except:
				tb.sendMessage(MY_CHAT_ID, 'You need give two numbers (/numrand min,max)')
			try:	
				min_max = list(map(int, raw.split(',')))
				if min_max[0] > min_max[1]:
					tb.sendMessage(MY_CHAT_ID, 'Make you sure put min,max')
					pass
				else:
					num = randint(min_max[0],min_max[1])
					tb.sendMessage(MY_CHAT_ID, str(num))
			except:
				tb.sendMessage(MY_CHAT_ID, 'Limits not found')
			
			prevCommand = command
			command = None
		elif '/exit' in command:
			shutdown()
			prevCommand = command
			command = None

		else:
			tb.sendMessage(MY_CHAT_ID, 'uh ni idea maestro')
			print(command)
			prevCommand = command
			command = None
	else:
		#tb.sendMessage(MY_CHAT_ID, 'desea repetir el ultimo comando?')
		print('Waiting for a new command.')
		command = None


while True:
    if args.RUN_TEST == 'true':
        run_test()
    elif args.RUN_TEST == 'false':
    	command = tb.readLastMessage()['message']
    	print('The command is: ' + command)
    	checkCommands(command)
    	time.sleep(1)
    else:
    	exit()
