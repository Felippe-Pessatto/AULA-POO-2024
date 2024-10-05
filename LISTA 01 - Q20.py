"CALCULAR O IMC (ÍNDICE DE MASSA CORPORAL): PEÇA O PESO (EM KG) E A ALTURA (EM METROS), E CALCULE O IMC USANDO A FÓRMULA: IMC = PESO (KG) / ALTURA (M)^2"

n1 = float(input("Informe seu peso em quilos: "))
n2 = float(input("Informe sua altura em metros: "))
print("Seu Índice de Massa Corporal é",round((n1/(n2**2)),2),"kg/m²")