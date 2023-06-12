from .class_patient import *
import datetime
from datetime import datetime
import time

#Registra o usuário
def register(registered):
		counter = 0
		print('Você escolheu cadastrar um paciente\n')
		user_input1 = input('Digite o nome do paciente\n')
		while True: #Verifica se foi digitado números
			try:
				user_input2 = int(input('Digite o telefone do paciente\n'))
				break
			except:
				print('Por favor, use apenas números')
		for i in registered: #Verifica se o número inserido já foi cadastrado
			if registered[counter].phone == user_input2:
				print('Número de telefone já cadastrado')
				break
			counter += 1
		else: #Se o número não é duplicado cria o usuário
			nowregistering = patient(user_input1, user_input2)
			registered.append(nowregistering)
			print('Paciente cadastrado com sucesso!')

#Lista todos os usuários cadastrados
def listusers(registered):
	counter = 0
	for i in registered:
		print(counter, registered[counter].name, registered[counter].phone)
		counter += 1

#Marca uma consulta
def setappointment(registered):
	currenttime = datetime.now() #Pega o datetime atual
	currenttimestamp = currenttime.timestamp() #Pega o timestamp atual
	counter = 0
	while True: #Verifica se o que foi digitado é um número e é um paciente da lista
		try:
			user_input1 = int(input('Escolha o paciente para o qual deseja marcar a consulta\n'))
			print('Você escolheu o paciente: ' + registered[user_input1].name)
			break
		except:
			print('Por favor, escolha um paciente da lista')

	while True: #Verifica se a data escolhida é válida
		try:
			inputdate = str(input('Por favor, escolha uma data usando o formato DD/MM/AAAA hh, por exemplo 12/06/2026 14\n'))
			datetimechosen = datetime.strptime(inputdate, "%d/%m/%Y %H")
			timestamp = datetimechosen.timestamp()
			break
		except:
			print('Escreva uma data válida, no formato pedido')

	specialty = input('Por favor, escreva a especialidade do médico desejada\n')

	for i in registered: #Verifica se a data escolhida está preenchida ou é inválida
		if timestamp == registered[counter].timestamp or timestamp <= currenttimestamp:
			print('Horário ou data indisponível')
			break
		counter +=1
	else: #Cria a consulta
		registered[user_input1].timestamp = timestamp
		registered[user_input1].specialty = specialty
		print('Você agendou uma consulta para o paciente: ' + registered[user_input1].name + ' na data: ')
		print(datetime.fromtimestamp(registered[user_input1].timestamp))