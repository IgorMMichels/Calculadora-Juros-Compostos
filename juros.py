valorInicial = float(input("Informe o aporte"))
valorMensal = float(input("Informe quantos reais você investirá mensalmente."))
porcentagem = int(input("Informe a porcentagem mensal do investimento."))
meses = int(input("Por quantos meses você irá investir?"))
valorFinal = valorInicial

for i in range(0, meses):
    valorMensal += (valorMensal) / 100 * porcentagem
    valorFinal += valorMensal
    print(i + valorFinal)
    