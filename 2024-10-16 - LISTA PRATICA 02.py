# 1. NÚMERO POSITIVO OU NEGATIVO: PEÇA AO USUÁRIO UM NÚMERO E INFORME SE ELE É POSITIVO, NEGATIVO OU ZERO.

n1 = float(input(f"Digite um número: "))
if n1 > 0:
    print("O número é positivo.")
elif n1 < 0:
    print("O número é negativo.")
else:
    print("O número é ZERO.")

# 2. MAIORIDADE: PEÇA A IDADE DO USUÁRIO E INFORME SE ELE É MAIOR DE IDADE (18 ANOS OU MAIS).

idade = int(input(f"Digite a sua idade: "))
if idade >= 18:
    print("Você é maior de idade. Parabéns você já pode ser preso.")

# 3. PAR OU ÍMPAR: PEÇA UM NÚMERO AO USUÁRIO E INFORME SE ELE É PAR OU ÍMPAR.

n1 = float(input(f"Digite um número: "))
if (n1 % 2) == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 4. NÚMERO MAIOR: PEÇA AO USUÁRIO DOIS NÚMEROS E INFORME QUAL É O MAIOR.

n1 = float(input(f"Digite um número: "))
n2 = float(input(f"Digite outro número: "))
if n1 > n2:
    print(f"O número {n1:,} é maior que o número {n2:,}.")
elif n1 < n2:
    print(f"O número {n2:,} é maior que o número {n1:,}.")
else:
    print("Informe números diferentes.")

# 5. DESCONTO DE COMPRA: PEÇA AO USUÁRIO O VALOR DE UMA COMPRA. SE O VALOR FOR MAIOR QUE R$ 100,00 APLIQUE UM DESCONTO DE 10%. CASO CONTRÁRIO, EXIBA O VALOR SEM DESCONTO.

n1 = float(input(f"Digite o valor da sua compra: "))
if n1 > 100:
    print(f"O valor total da compra é de: R$ {n1*(1-(10/100)):,.2f} reais")
else:
    print(f"O valor total da compra é de: R$ {n1:,.2f} reais")

# 6. VERIFICAR MÚLTIPLO: PEÇA AO USUÁRIO UM NÚMERO E VERIFIQUE SE ELE É MÚLTIPLO DE 5.

n1 = float(input(f"Digite um número: "))
if (n1 % 5) == 0:
    print("O número é múltiplo de cinco.")
else:
    print("O número não é múltiplo de cinco.")

# 7. CÁLCULO DE MÉDIA: PEÇA TRÊS NOTAS AO USUÁRIO E CALCULE A MÉDIA. SE A MÉDIA FOR MAIOR OU IGUAL A 7, INFORME QUE O ALUNO FOI APROVADO, SENÃO, REPROVADO.

n1 = float(input(f"Digite a primeira nota: "))
n2 = float(input(f"Digite a segunda nota: "))
n3 = float(input(f"Digite a terceira nota: "))

if ((n1+n2+n3)/3) >= 7:
    print(f"O aluno(a) foi aprovado(a).")
else:
    print(f"O aluno(a) foi reprovado(a).")

# 8. SENHA CORRETA: CRIE UM PROGRAMA QUE PEÇA UMA SENHA AO USUÁRIO. SE A SENHA FOR "python123_EFG", exiba "Acesso permitido". Caso contrário, "Senha incorreta".

senha = input(f"Digite a sua senha: ")
if senha == "python123_EFG":
    print(f"Acesso permitido.")
else:
    print(f"Senha incorreta.")

# 9. ENTRADA GRATUITA: PEÇA AO USUÁRIO SUA IDADE E INFORME SE ELE TEM DIREITO A ENTRADA GRATUITA (IDADE MENOR QUE 5 ANOS OU MAIOR QUE 60 ANOS).

idade = int(input(f"Digite a sua idade: "))
if idade < 5:
    print("Você tem direito à entrada gratuita.")
elif idade > 60:
    print("Você tem direito à entrada gratuita.")
else:
    print("Você não tem direito à entrada gratuita.")

# 10. VERIFICAR NOTA: PEÇA UMA NOTA ENTRE 0 E 10 AO USUÁRIO. SE O VALOR FOR INVÁLIDO, EXIBA UMA MENSAGEM DE ERRO.

n1 = int(input(f"Digite uma nota de 0 a 10, por favor: "))
if n1 >= 0 and n1 <= 10:
    None
else:
    print(f"Erro. O número digitado é inválido.")

# 11. CATEGORIA DE IDADE: PEÇA A IDADE DO USUÁRIO E INFORME SE ELE É "CRIANÇA" (MENOS DE 12 ANOS), "ADOLESCENTE" (ENTRE 12 E 17 ANOS) OU "ADULTO" (18 OU MAIS).

idade = int(input(f"Digite a sua idade: "))
if idade < 12:
    print(f"Você é uma criança.")
elif idade >= 12 and idade <= 17:
    print(f"Você é um adolescente.")
else:
    print(f"Você é um adulto.")

# 12. MAIOR DE TRÊS NÚMEROS: PEÇA TRÊS NÚMEROS AO USUÁRIO E INFORME QUAL É O MAIOR.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
if n1 > n2 and n1 > n3:
  print(f"O primeiro número é o maior.")
elif n2 > n1 and n2 > n3:
  print(f"O segundo número é o maior.")
else:
  print(f"O terceiro número é o maior.")

# 13. DIVISÃO SEGURA: PEÇA DOIS NÚMEROS AO USUÁRIO E DIVIDA O PRIMEIRO PELO SEGUNDO. SE O SEGUNDO NÚMERO DIGITADO FOR ZERO, INFORME QUE A DIVISÃO NÃO É POSSÍVEL.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
if n2 == 0:
  print(f"A divisão não é possível.")
else:
  print(f"O resultado da divisão é: {(n1/n2)}")

# 14. NÚMERO DENTRO DE INTERVALO: PEÇA AO USUÁRIO UM NÚMERO E VERIFIQUE SE ELE ESTÁ ENTRE 10 E 50.

n1 = float(input("Digite um número: "))
if n1 >= 10 and n1 <= 50:
  print(f"O número {n1} está entre 10 e 50.")
else:
  print(f"O número {n1} não está entre 10 e 50.")

# 15. APROVADO, RECUPERAÇÃO OU REPROVADO: PEÇA A MÉDIA DO ALUNO E INFORME SE ELE ESTÁ "APROVADO" (MÉDIA >= 7), "EM RECUPERAÇÃO" (5 <= MÉDIA < 7) OU "REPROVADO" (MÉDIA < 5).

n1 = float(input("Digite a sua nota média: "))
if n1 >= 7:
  print(f"Aprovado.")
elif 5 <= n1 < 7:
  print(f"Em recuperação.")
elif n1 < 5:
  print(f"Reprovado.")
else:
  None

# 16. CALCULAR IMC: PEÇA AO USUÁRIO SEU PESO E ALTURA, CALCULE O IMC E INFORME SE ELE ESTÁ "ABAIXO DO PESO" (IMC < 18.5), "PESO NORMAL" (18.5 <= IMC < 25) OU "ACIMA DO PESO" (IMC >= 25).

peso = float(input(f"Digite o seu peso: "))
altura = float(input(f"Digite a sua altura: "))
imc = (peso/(altura**2))
if imc < 18.5:
  print(f"Você está abaixo do peso.")
elif 18.5 <= imc < 25:
  print(f"Você está com peso normal.")
elif imc >= 25:
  print(f"Você está acima do peso.")
else:
  None

# 17. IDENTIFICAR TRIÂNGULO: PEÇA AO USUÁRIO TRÊS LADOS E VERIFIQUE SE ELES PODEM FORMAR UM TRIÂNGULO. CASO POSSAM, INFORME SE O TRIÂNGULO É "EQUILÁTERO", "ISÓSCELES" OU "ESCALENO".

lado1 = float(input(f"Digite o primeiro lado: "))
lado2 = float(input(f"Digite o segundo lado: "))
lado3 = float(input(f"Digite o terceiro lado: "))
if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
  print(f"O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  print(f"O triângulo é isósceles.")
else:
  print(f"O triângulo é escaleno.")

# 18. LOGIN E SENHA: PEÇA AO USUÁRIO UM NOME DE USUÁRIO E SENHA. VERIFIQUE SE O NOME DE USUÁRIO É "admin" E A SENHA É "1234". CASO AMBOS ESTEJAM CORRETOS, INFORME "LOGIN BEM-SUCEDIDO".

login = input(f"Digite seu nome de usuário: ")
senha = input(f"Digite sua senha: ")
if login == "admin" and senha == "1234":
  print(f"Login bem-sucedido.")
else:
  print(f"Login mal-sucedido.")

# 19. VERIFICAR MAIORIDADE PARA DIRIGIR: PEÇA A IDADE DO USUÁRIO E VERIFIQUE SE ELE PODE DIRIGIR (18 ANOS OU MAIS). SE TIVER MENOS DE 18, INFORME QUANTOS ANOS FALTAM PARA ELE PODER DIRIGIR.

idade = int(input(f"Digite a sua idade: "))
if idade >= 18:
  print(f"Você já pode dirigir.")
else:
  print(f"Ainda falta(m) {(18-idade)} ano(s) para você dirigir.")
