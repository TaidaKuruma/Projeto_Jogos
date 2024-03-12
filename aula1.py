ValorA = int(input("Digite o primeiro numero \n"))
valorB = int(input("Digite o secundo numero \n"))
ValorC = int(input("Digite o terceiro numero \n"))

operacao = int(input("escolha a sua operacao.\n 1 = soma\n 2 = subtracao \n 3 = multiplicacao\n 4 = divisao\n"))

if operacao == 1:
    print("a sua soma deu o resultado de", ValorA + valorB + ValorC)
elif operacao == 2:
    print("a sua subtracao deu o resultado de", ValorA - valorB - ValorC)
elif operacao == 3:
    print("a sua multiplicacao deu o resultado de", ValorA * valorB * ValorC)
elif operacao == 4:
    print("a sua divisao deu o resultado de", ValorA / valorB / ValorC)
else:
    print("invalido seu burro")
