# Algorítmo para Prova 1 de Fundamentos da Computação
# Professor Sofiane Labidi
# Aluna: Tarsila Tereza Santos Pinheiro
# Universidade Federal do Maranhão
# Bacharelado Interdisciplinar em Ciência e Tecnologia
# 20/11/2023

# Crie três vetores. Os valores devem ser adicionados até o usuário digitar um valor negativo. Faça a interseção, a união e diferença.

vetor1 = []
vetor2 = []
vetor3 = []


def adicionandoValores1():
	while True:

		valor = int(input("Digite um valor para o vetor [1]: "))

		if valor < 0:
			print("----"*10)
			break
		vetor1.append(valor)
		
def adicionandoValores2():
	while True:

		valor = int(input("Digite um valor para o vetor [2]: "))

		if valor < 0:
			break
			print("----"*10)
		vetor2.append(valor)

def adicionandoValores3():
	while True:

		valor = int(input("Digite um valor para o vetor [3]: "))

		if valor < 0:
			break
			print("----"*10)
		vetor3.append(valor)
adicionandoValores1()
adicionandoValores2()
adicionandoValores3()
print(vetor1)
print(vetor2)
print(vetor3)

conjunto1 = set(vetor1)
conjunto2 = set(vetor2)
conjunto3 = set(vetor3)

inter = conjunto1 & conjunto2 & conjunto3
intersecao = list(inter)
adicao = conjunto1 | conjunto2 | conjunto3
uniao = list(adicao)

print("Interseção: ", intersecao)
print("União: ", uniao)