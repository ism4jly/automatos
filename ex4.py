

# M = {Q, E, D, q0, F}

# Q = {q0, q1, q2, q3}
# E = {a, b}

# D = {
#   D: {q0, a -> q1}
#   D: {q1, a -> q1}
#   D: {q1, b -> q2}
#   D: {q2, b -> q1}
#   D: {q2, a -> q3}
# }

# q0 = q0
# F = {q3}


# havia visto algumas diferenças do deterministico para o não deterministico, e vi sobre o NFA ter o fecho epsilon, porém não entendi como aplica-lo em código.

#realizei apenas uma pequena alteração nesse código sobre o simbolo vazio ser &

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