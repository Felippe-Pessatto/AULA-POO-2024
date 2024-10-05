"DESCONTO PROGRESSIVO: PEÇA O VALOR DE UMA COMPRA E APLIQUE UM DESCONTO DE 5% SE O VALOR FOR MAIOR QUE R$100, E DE 10% SE FOR MAIOR QUE R$500."

n1 = float(input("Informe o valor da compra: "))
if n1>500:
    n2 = 10
elif n1>100:
    n2 = 5
else:
    n2 = 0
print("Você recebeu um desconto de",(n2),"%, o valor total da sua compra é de R$",round((n1*(1-(n2/100))),2),"reais")