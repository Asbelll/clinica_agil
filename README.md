# Descrição
Exercício de desenvolvimento de um sistema de clínica de consultas para a Aceleradora Ágil.

O sistema deve conter as seguintes funções:
- **Cadastrar um paciente**: O programa solicita o nome e o telefone do usuário. Após o
cadastro, exibe a mensagem "Paciente cadastrado com sucesso" e adiciona o paciente à
lista de Pacientes Cadastrados. Em seguida, retorna ao menu principal.
- **Marcações de consultas**: Ao selecionar essa opção, o programa exibe uma lista
numerada dos pacientes cadastrados. Ao escolher o número correspondente a um
paciente, solicita o dia, a hora e a especialidade desejada para a consulta. Após o envio
desses dados, o agendamento é adicionado à lista de agendamentos e o programa
retorna ao menu principal.
- **Cancelamento de consultas**: Ao selecionar essa opção, o programa exibe uma lista
numerada dos agendamentos existentes. Ao escolher o número correspondente ao
agendamento que deseja remarcar, é exibida uma mensagem informando a data, a hora e
a especialidade da consulta agendada. Nesse momento, o usuário pode optar por
cancelar a consulta. Ao confirmar o cancelamento, o agendamento é removido da lista e o
programa retorna ao menu principal.

Como desafio foi pedido para criar um banco de dados para o sistema.

# Decisões
Para conclusão do projeto foi utilizada a linguagem de programação Python.
Para a conclusão do desafio foi utilizado o módulo Pickle para escrever e ler o objeto que armazena os dados do paciente em um arquivo binário.

# Créditos
[Chrystian Álex Aguiar de Andrade](https://github.com/Asbelll)
