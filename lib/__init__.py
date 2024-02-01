def fcores(text='', cor='', fundo=False):
  '''
  -> Função que adiciona cores aos textos.
  :param arg: Texto que será editado
  :param cor: Cor adicionada ao texto
  :param fundo: Padrão False, se verdadeiro altera as cores de fundo
  :return: Texto formatado com a cor escolhida
  '''
  if fundo: 
    cores = {
      '' : f'\033[m{text}\033[m',
      'branco' : f'\033[40m{text}\033[m',
      'vermelho' : f'\033[41m{text}\033[m',
      'verde' : f'\033[42m{text}\033[m',
      'amarelo': f'\033[43m{text}\033[m',
      'azul': f'\033[44m{text}\033[m',
      'magenta': f'\043[35m{text}\033[m',
      'ciano': f'\033[46n{text}\033[m',
      'cinza' : f'\033[47m{text}\033[m'
    }
  else:
    cores = {
      '' : f'\033[m{text}\033[m',
      'branco' : f'\033[30m{text}\033[m',
      'vermelho' : f'\033[31m{text}\033[m',
      'verde' : f'\033[32m{text}\033[m',
      'amarelo': f'\033[33m{text}\033[m',
      'azul': f'\033[34m{text}\033[m',
      'magenta': f'\033[35m{text}\033[m',
      'ciano': f'\033[36n{text}\033[m',
      'cinza' : f'\033[37m{text}\033[m'
    }
  r = cores[cor]
  return r

def leia_int(text):
  '''
  -> Le um dado e aceita apenas números inteiros
  :param text: Texto exibido 
  '''
  while True:
    try:
      n=int(input(text))
      return n
    except:
      print(fcores('Erro! Favor digite apenas números inteiros.', 'vermelho'))
  


def func_cabecalho(text, linha='-', tam=25, cor='', fundo=False):
  '''
  -> Printa um cabeçalho com linhas ou dados acima e abaixo de um texto centralizado
  :param text: Texto centralizado exibido
  :param linha: Caracter printado acima e abaixo do texto
  :param tam: Tamanho do cabecalho
  :param cor: Cor do cabecalho
  :return : 0
  '''
  print(fcores(linha*tam, cor, fundo))
  print(fcores(text.center(tam), cor, fundo))
  print(fcores(linha*tam, cor, fundo))

def func_menu(args):
  '''
  -> Cria um menú.
  :param args: Itens que compõe o menú
  :return :apenas um inteiro escolhido
  '''
  for i, c in enumerate(args):
    print(fcores(i+1, 'amarelo'), ' - ', fcores(c, 'azul'))
  print('-'*25)
  

def func_interface(text, args):
  '''
  -> Printa uma interface visual em forma de menu.
  :param text: Texto exibido no menu principal formatado
  :param cor: Cor do menu principal
  :param args: lista contendo os itens do menu
  :return: 0
  '''
  func_cabecalho(text, linha='*', cor='cinza')
  func_menu(args)


def func_pessoascadastradas():
  '''
  -> Lê o arquivo e printa os dados
  :raturn: 0
  '''
  with open('cadastro.txt', 'r') as arquivo:
    print(f'{"NOME":19}{"IDADE"}')
    for linha in arquivo:
      s = linha.find(',')  # Separador
      print(f'{linha[:s]:19}{linha[s+1:]:>5}', end='')
def func_cadastrapessoas():
  '''
  -> Acidiona uma pessoa no cadastro.txt
  :return: 0
  '''
  with open('cadastro.txt', 'a') as arquivo:
    nome=input('Nome: ')
    idade=leia_int('Idade: ')
    arquivo.write(f'{nome},{idade}\n')
  print(fcores(f'{nome} cadastrado(a) com sucesso!', 'verde'))


