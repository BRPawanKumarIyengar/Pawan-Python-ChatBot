from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
import win32com.client as Bolna

Vaachal = Bolna.Dispatch('SAPI.SpVoice')

Batuni = ChatBot('Test')
Batuni.set_trainer(ListTrainer)

for Text_Files in os.listdir('yo'):
	Baat_Cheet = open('yo/' + Text_Files,'r').readlines()
	Batuni.train(Baat_Cheet)
	print(Baat_Cheet)

print('Batuni:  Hello! I am Batuni .... the chatbot. I would love to chat with you')
Vaachal.Speak('Hello! I am Batuni .... the chatbot. I would love to chat with you')

while True:
	request = input ('You:  ')
	if request == 'bye':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
		
	if request == 'Bye':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
		
	if request == 'Exit':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
	
	if request == 'exit':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
		
	if request == 'terminate':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
		
	if request == 'terminate':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
	
	if request == 'GoodBye':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
	
	if request == 'goodbye':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
	
	if request == 'Good Bye':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
	
	if request == 'good bye':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
	
	if request == 'Stop Chat':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
	
	if request == 'stop chat':
		print('chat shall now terminate ... GoodBye!')
		Vaachal.Speak('chat shall now terminate ... GoodBye!')
		break
	
	response = Batuni.get_response(request)
	print('Batuni:  ', response)
	Vaachal.Speak(response)