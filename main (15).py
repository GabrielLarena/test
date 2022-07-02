
L = [] #paradas em cartesiano#
R = [] #ponto do restalrante#
a = int(input("quantidade de paradas: "))

x = int(input("X da entrada e saida: "))
y = int(input("Y da entrada e saida: "))
R.append((x, y))

for i in range(0, a):
    x = int(input("X da parada " + str(i+1) + ": "))
    y = int(input("Y da parada " + str(i+1) + ": "))
    
    L.append((x, y))
fim=10000
caminho=()

#permutação#
def per(lis):
  
  #permutação de 0 numeros#
  if len(lis) == 0:
    return []
  
  #permutação de 1 numero#
  if len(lis) == 1:
    return [lis]

  permutações = [] #lista vazia para adicionar ao resultado final#

  #pertação de um numero qualquer#
  for i in range(len(lis)):
    #trancar o numero i#
    t = lis[i]
    #retirar o i da lista#
    rlis = lis[:i] + lis[i + 1:]
    #permutar o resto dos numeros#
    for p in per(rlis):
      #deletar caminhos iguais#
      if len([t] + p) == 4 and (list(reversed([t] + p))) in l:
        continue
      permutações.append([t] + p)    
  
  return permutações

#calcular distancia entre dois pontos#
def dis(X, Y):
   return abs(X[0] - Y[0]) + abs(X[1] - Y[1])

#calcular todas possibilidades por permutação#

for i in per(L):
  
  val = 0
  #calcular a distancia entre todos os pontos da per#
  for j in range(0, a-1):
    val = val + dis(i[j], i[j + 1])
  #adicionar a distancia entre o incio e fim ao restalrante#
  val = val + dis(R[0], i[0])
  val = val + dis(i[a-1], R[0])
  
  #checar se o caminho é o melhor e salvar o resultado#
  if val < fim:
    fim = val
    caminho = i
    
print(fim)
print(caminho)