#Nomes:Lucas Feliciano da Silva     RA:182487
#      Nicolas de Sousa Imagawa     RA:204147

#Porta dos Desesperados - Probabilidade de Acerto sem troca de porta.

import random
import matplotlib.pyplot as plt

v = []
prob = []

i = 0
n = 50000
a = [0, 0 ,1]
b = [0, 0 ,1]

while i < n:
    random.shuffle(a)
    random.shuffle(b)
    if a == b:
        v.append(1)
    prob.append(sum(v)/(i + 1))
    i += 1

plt.plot(range(0, n), prob, label= 'Não trocou de porta')
plt.legend()
plt.title("Análise do Problema de Monty Hall")
plt.xlabel("Número de tentativas")
plt.ylabel("Probabilidade acumulada de acertos")
plt.show()