#FORCAAAAAAAAAAAAAAAA
import random
def jogar():
    escolha = int(input("POR FAVOR ESCOLHA COM O QUE VC QUER SOFRER.\n 1-nomes\n 2-jogos\n 3-animes\n"))
    
    if escolha == 1:
        sorteio_palavra_int = random.randint(1,5)
        palavras = []
        arquivo = open("nomes.txt", "r")
        for linha in arquivo:
            palavras.append(linha.strip())
        palavra_secreta = random.choice(palavras)

    elif escolha == 2:
        sorteio_palavra_int = random.randint(1,5)
        palavras = []
        arquivo = open("jogos.txt", "r")
        for linha in arquivo:
            palavras.append(linha.strip())
        palavra_secreta = random.choice(palavras)

    elif escolha == 3:
        sorteio_palavra_int = random.randint(1,5)
        palavras = []
        arquivo = open("animes.txt", "r")
        for linha in arquivo:
            palavras.append(linha.strip())
        palavra_secreta = random.choice(palavras)
    
    print("JOGANDO FORCAAAAAAAAAA")
    
    #if sorteio_palavra_int == 1:
        #palavra_secreta = "amicus"
    #elif sorteio_palavra_int == 2:
        #palavra_secreta = "loken"
    #elif sorteio_palavra_int == 3:
        #palavra_secreta = "shoichi"
    #elif sorteio_palavra_int == 4:
        #palavra_secreta = "shu chi"
    #elif sorteio_palavra_int == 5:
        #palavra_secreta = "walter"

    vidas = 5
    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append("_")
    acertou = False
    errou = False

    while(not acertou and not errou):
        print(letras_acertadas)
        print("TU TEM", vidas, "VIDAS AINDA")
        chute = input("Digite a letrinha.\n")
        print("Chutaste...", chute)

        index = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = chute
                index = index + 1
        else:
            vidas = vidas - 1

        if letras_acertadas.count("_") == 0:
            
            acertou = True
        
        if vidas < 1:
            errou = True
        
        if acertou == True:
            print("CABOU AMIGUINHOOO, A PALAVRA FOI", palavra_secreta)
        if errou == True:
            print("BURRO DEMAIS, TU PERDEU")
if (__name__ == "__main__"):
    jogar()