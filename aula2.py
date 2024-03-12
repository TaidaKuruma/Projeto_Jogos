import random

print("O JOGO DE LA DIVINHACAO!!!! YIPPE!!!!")
sorteio1 = random.randint(0, 100)
sorteio2 = random.randint(0, 100)

chances = 1
max_chances = 10
while(chances <= max_chances) :
    chute = int(input("Tentativa {} de {}.\n o que vc chuta? os numeros sao entre 0 e 10. \n".format(chances, max_chances)))
    acertou = chute == sorteio1

    if (acertou) :
        print("ACERTOU MIZERAVI")
        sorteio1 = acertou
    elif (chute > sorteio1) :
        print("O NUMERO E MENOR SEU BURRO")
    elif (chute < sorteio1) :
        print("O NUMERO E MAIOR SEU MONGOLOIDE")
    chances = chances + 1

    if sorteio1 == acertou :
        chances = 1
        chute2 = int(input("Tentativa {} de {}.\nO que vc chuta este este é o segundo sorteio? os numeros sao entre 0 e 10. \n".format(chances, max_chances)))
        acertou2 = chute2 == sorteio2
        
        if (acertou2) :
            print("ACERTOU DE NOVO MIZERAVI")
        elif (chute2 > sorteio2) :
            print("O NUMERO E MENOR SEU BURRO")
        elif (chute2 < sorteio2) :
            print("O NUMERO E MAIOR SEU MONGOLOIDE")
        chances = chances + 1

if (chances > 3) :
    print("Vc perdeu.")
