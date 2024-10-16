# 1. VERIFICAÇÃO DE MAIORIDADE: INFORME IDADE E INFORMAR SE É MAIOR OU MENOR DE IDADE.

idade = int(input(f"Digite a sua idade: "))
if idade >= 18:
    print("Você é maior de idade. Parabéns você já pode ser preso.")
else:
    print("Você é menor de idade.")

# 2. USUÁRIO INFORMA DOIS NÚMEROS ALEATÓRIOS, E O SISTEMA VAI COMPARAR SE OS NÚMEROS SÃO IGUAIS OU DIFERENTES.

n1 = float(input(f"Digite um número: "))
n2 = float(input(f"Digite outro número: "))

if n1 == n2:
    print("Os números são iguais.")
else:
    print("Os números são diferentes.")

# 3. VERIFICAR SE UM NÚMERO É POSITIVO, NEGATIVO OU ZERO.

n1 = float(input(f"Digite um número: "))

if n1 > 0:
    print("O número é positivo.")
elif n1 < 0:
    print("O número é negativo.")
else:
    print("O número é ZERO.")