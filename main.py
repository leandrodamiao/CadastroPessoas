from time import sleep
from lib import *

try:
  with open('cadastro.txt', 'r') as arquivo:
    print(fcores('...', 'verde'))
except:
  with open('cadastro.txt', 'x') as arquivo:
    print(fcores('Arquivo não encontrado,\nEstamos criando um para você.'))
    sleep(1.5)
 
   

lista_opcoes = ['Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair']

while True:
  func_interface('Menu Principal', lista_opcoes )
  match leia_int(fcores('Opção: ', 'verde')):
    case 1:
      print('')
      func_cabecalho('Pessoas Cadastradas')
      func_pessoascadastradas()
      sleep(2)

    case 2:
      print('')
      func_cabecalho('cadastrar pessoas')
      func_cadastrapessoas()
      sleep(2)

    case 3:
      print('')
      func_cabecalho('Saindo do sistema')
      for c in range (0, 3):
        print('.', end='', flush=True)
        sleep(1)
      print(fcores('\nVolte sempre', 'amarelo'))
      break
    case _:
      print(fcores('Erro! Opção inválida.', 'vermelho'))
      continue

