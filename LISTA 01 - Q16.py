"PREÇO COM DESCONTO: PEÇA O PREÇO DE UM PRODUTO E O PERCENTUAL DE DESCONTO, E MOSTRE O PREÇO FINAL COM DESCONTO APLICADO."

n1 = float(input("Informe o preço do produto: "))
n2 = float(input("Informe o percentual do desconto: "))
print("O preço final com desconto é: R$",(n1*(1-(n2/100))), "reais")