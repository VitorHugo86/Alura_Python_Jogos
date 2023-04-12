import random
import os 

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    print(
        '\n[1] Facil '
        '\n[2] Medio '
        '\n[3] Dificil'
        '\n ')

    nivel = int(input('Escolha o nivel: '))
    numero_secreto = random.randrange(1,51)
    total_de_tentativas = 0
    pontos = 1000

    if nivel == 1:
        total_de_tentativas = 20
        os.system('cls')
        print('Jogo de adivinhação \nNivel: Facil')
    elif nivel == 2:
        total_de_tentativas = 10
        os.system('cls')
        print('Jogo de adivinhação \nNivel: Medio')
    elif nivel == 3:
        total_de_tentativas = 5
        os.system('cls')
        print('Jogo de adivinhação \nNivel: Dificil')

        


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 50: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 501):
            print("Você deve digitar um número entre 1 e 50!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            os.system('cls')
            print("Você acertou!")
            print(f'Você fez {pontos} pontos')
            break
        else:
            os.system('cls')
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if rodada == total_de_tentativas:
                    os.system('cls')
                    print(f'O numero secreto era {numero_secreto}. Você fez {pontos} pontos ')

    print("Fim do jogo")
if __name__ == '__main__':
    jogar()