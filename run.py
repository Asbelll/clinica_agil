#Opções que deve conter:
#Cadastrar: é pedido o nome e o número de telefone, após o cadastro deve exibir a mensagem "Paciente cadastrado com sucesso"
#Marcações de consultas: o programa vai exibir a lista de pacientes cadastrados, escolhendo o número do paciente o programa pedirá o dia, hora e especialidade do médico para a consulta, exibir mensagem de feedback e adicionar	a lista de agendamentos
#Cancelamento de consultas: é exibido a lista de consultas, ao escolher o número da consulta desejada, irá ser exibido suas informações (data, hora e especialidade) e então é dada a opção de cancelar a consulta ou voltar, novamente é exibida uma mensagem de feedback

#Coisas para se manter em mente:
#Não pode cadastrar o mesmo paciente mais de uma vez (usar o número de telefone único para cada paciente), caso contrário exibir mensagem "Paciente já cadastrado"
#Não pode marcar mais de uma consulta para o mesmo horário
#Não pode marcar consulta antes da data atual

#Armazenar as informações em um "banco de dados", utilizando I/O
from modules.class_patient import *
from modules.function_register import *
import time
import datetime
from datetime import datetime

registered = []

while True:
	user_input = input(
		'Olá, seja bem vindo!\nEscolha a operação desejada:\n1) Cadastrar paciente\n2) Marcar consulta\n3) Cancelar consulta\n0) Sair\n')

	if user_input == '1':
		register(registered)
		continue

	elif user_input == '2':
		print('Você escolheu marcar uma consulta\n')
		listusers(registered)
		setappointment(registered)
		continue

	elif user_input == '3':
		print('Você escolheu cancelar uma consulta')
		cancelappointment(registered)
		continue

	elif user_input == '0':
		break

	else:
		print('Digite o número de uma das operações listadas')
		continue