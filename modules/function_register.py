from .class_patient import *
import datetime
from datetime import datetime
import time
import pickle

#Registra o usuário
def register(registered):
		counter = 0

		print('Você escolheu cadastrar um paciente\n')

		user_input1 = input('Digite o nome do paciente\n')
		if user_input1.strip() == '':
			print('Nome digitado inválido')
			return

		try: #Verifica se foi digitado números
			user_input2 = int(input('Digite o telefone do paciente\n'))
		except:
			print('Número digitado inválido')
			return

		for i in registered: #Verifica se o número inserido já foi cadastrado
			if registered[counter].phone == user_input2:
				print('Número de telefone já cadastrado')
				break
			counter += 1
		else: #Se o número não é duplicado cria o usuário
			nowregistering = patient(user_input1, user_input2)
			registered.append(nowregistering)
			write(registered)
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

	try: #Verifica se o que foi digitado é um número e é um paciente da lista
		user_input1 = int(input('Escolha o paciente para o qual deseja marcar a consulta: \n'))
		print('Você escolheu o paciente: ' + registered[user_input1].name)
	except:
		print('Paciente escolhido inválido')
		return

	try: #Verifica se a data escolhida é válida
		inputdate = str(input('Por favor, escolha uma data usando o formato DD/MM/AAAA hh, por exemplo 12/06/2026 14: \n'))
		datetimechosen = datetime.strptime(inputdate, "%d/%m/%Y %H")
		timestamp = datetimechosen.timestamp()
	except:
		print('Data escolhida inválida')
		return

	specialty = input('Por favor, escreva a especialidade do médico desejada: \n')

	for i in registered: #Verifica se a data escolhida está preenchida ou é inválida
		if timestamp == registered[counter].timestamp or timestamp <= currenttimestamp:
			print('Horário ou data indisponível')
			return
		counter +=1
	else: #Cria a consulta
		registered[user_input1].timestamp = timestamp
		registered[user_input1].specialty = specialty
		write(registered)
		print('Você agendou uma consulta para o paciente: ', registered[user_input1].name, ' na data: ', datetime.fromtimestamp(registered[user_input1].timestamp))

#Cancela uma consulta
def cancelappointment(registered):
	counter = 0
	for i in registered:
		if registered[counter].timestamp != '':
			print('Número: ', counter, end=' ')
			print('Paciente: ', registered[counter].name, end=' ')
			print('Telefone: ', registered[counter].phone, end=' ')
			print('Data e hora: ', datetime.fromtimestamp(registered[counter].timestamp))
			counter += 1
		else:
			counter += 1

	try:
		user_input1 = int(input('Digite o número do paciente desejado: '))
	except:
		print('Número inválido')
		return

	try:
		if registered[user_input1]:
			if registered[user_input1].timestamp != '':
				registered[user_input1].timestamp = ''
				registered[user_input1].specialty = ''
				write(registered)
			else:
				print('O número do paciente digitado não possui uma consulta agendada')
				return
	except:
		print('O paciente escolhido não existe')
		return

def write(registered):
	with open('database.pkl', 'wb') as file:
		pickle.dump(registered, file)