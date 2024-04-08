import aula1
import aula2
import aula3

jogo = int(input("Que jogo vc quer caramba?\n 1 - Calculadora foda\n 2 - adivinhação foda\n 3 - forca foda\n"))

if jogo == 1:
    print("executando a calculadora catapimbas.")
    aula1.jogar()

if jogo == 2:
    print("executando a adivinhação caramba")
    aula2.jogar()

if jogo == 3:
    print("executando a forca caramba")
    aula3.jogar()