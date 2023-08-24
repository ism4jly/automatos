
print("1 - Aceitação de Automatos")
print("2 - Conversão de AFD para AFND")
opc = input("Qual opção deseja executar? ")


def converterAFDtoAFND(afd):
    afnd = {
      "estados": afd["estados"],
      "alfabeto": afd["alfabeto"],
      "transicoes": {},
      "estado_inicial": afd["estado_inicial"],
      "estados_aceitacao": afd["estados_aceitacao"]
    }

    for estado in afd["estados"]:
      afnd["transicoes"][estado] = {}

      for simbolo in afd["alfabeto"]:
        proximos_estados = [afd["transicoes"][estado][simbolo]]
        afnd["transicoes"][estado][simbolo] = proximos_estados

    return afnd

estados = set(input("Digite os estados do autômato separados por vírgula: ").split(','))
alfabeto = set(input("Digite o alfabeto do autômato separado por vírgula: ").split(','))

transicoes = {}
for estado in estados:
    transicoes_estado = {}
    for simbolo in alfabeto:
        prox_estado = input(f"Digite o próximo estado para {simbolo} a partir de {estado}: ")
        transicoes_estado[simbolo] = prox_estado
    transicoes[estado] = transicoes_estado

estado_inicial = input("Digite o estado inicial do autômato: ")
estados_aceitacao = set(input("Digite os estados de aceitação do autômato separados por vírgula: ").split(','))



afd = {
    "estados": estados,
    "alfabeto": alfabeto,
    "transicoes": {
        transicoes
    },
    "estado_inicial": estado_inicial,
    "estados_aceitacao": estados_aceitacao
}

# Converter AFD para AFND
afnd = converterAFDtoAFND(afd)

print('1 - Visualizar AFD')
print('2 - Visualizar AFND')


mostrar = input("Deseja visualizar qual das opções? ")

if mostrar == '1':
  print("AFD:")
  print(afd)
elif mostrar == '2':
  print("\nAFND:")
  print(afnd)
else:
  print('Opção incorreta')


# ------------------------//-------------------------------


def automatos():
  # estrutura
  estados = []
  alfabeto = []
  func_transicao = {}
  estado_inicial = ""
  estados_aceitacao = []


  # dados do automato
  
  print("Informe o conjunto de estados: ", end='')
  estados = input().split()
  
  print("Informe o alfabeto de estados: ", end='')
  alfabeto = input().split()
  
  print('Informe o estado inicial: ', end='')
  estado_inicial = input()
  
  print("Informe o conjunto de estados de aceitação: ", end='')
  estados_aceitacao = input().split()
  
  print("Defina as funções de transição: ")
  for estado in estados:
    for simbolo in alfabeto:
      print(f"\t {simbolo}")
      print(f"{estado}\t------>\t", end='')
      proximo_estado = input()
  
      if proximo_estado == ".":
        func_transicao[(estado, simbolo)] = None
      else:
        func_transicao[(estado, simbolo)] = proximo_estado
        # não deterministico
        if simbolo == '&':
          simbolo = ''
        func_transicao[(estado, simbolo)] = proximo_estado
  
  
  # reconhecendo linguagens
  print("Informe a linguagem a ser reconhecida: ", end="")
  entrada = input()
  
  estado_atual = estado_inicial
  
  for simbolo in entrada:
    print(f"Estado atual: {estado_atual}")
    print(f"Entrada atual: {simbolo}")
    print(f"Próximo estado: {func_transicao[(estado_atual, simbolo)]}")
  
    estado_atual = func_transicao[(estado_atual, simbolo)]
  
    if estado_atual == None:
      print("O automato nao reconheceu a linguagem")
      break
  
  if estado_atual in estados_aceitacao:
    print("Reconheceu")
  else:
    print("Não Reconheceu")


if opc == '1':
  automatos()
