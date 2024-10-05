"FÓRMULA DE BHASKARA: PEÇA OS COEFICIENTES AAA, BBB E CCC DE UMA EQUAÇÃO DO SEGUNDO GRAU E CALCULE AS RAÍZES USANDO A FÓRMULA DE BHASKARA."

n1 = float(input("Informe um valor para a: "))
n2 = float(input("Informe um valor para b: "))
n3 = float(input("Informe um valor para c: "))
delta = (n2**2)-(4*n1*n3)
print("As raízes são x1:",((-n2+(delta**(1/2)))/(2*n1)),"e x2:",((-n2-(delta**(1/2)))/(2*n1)))