import os
import random


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    min_chute = 1
    max_chute = 100
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    while True:
        try:
            nivel = int(input("Defina o nível: "))
            if nivel not in [1, 2, 3]:
                print('Opção inválida. Por favor escolha entre as opções.')
            else:
                break
        except ValueError:
            print('Entrada inválida. Por favor digite um número inteiro.')
        
        if (nivel == 1):
            total_de_tentativas = 20
        elif (nivel == 2):
            total_de_tentativas = 10
        else:
            total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        # Validar entrada do usuário para o chute
        while chute < min_chute or chute >= max_chute:
            print(f"Você deve digitar um número entre {min_chute} e {max_chute}!")
            chute_str = input(f"Digite um número entre {min_chute} e {max_chute}: ")
            chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            os.system('cls')
            print(f'O numero era {numero_secreto}')
            print("Você acertou e fez {} pontos!".format(pontos))
            imprime_mensagem_vencedor()
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    os.system('cls')
    print("Fim do jogo")
    print(f'O numero era {numero_secreto}')
    imprime_mensagem_perdedor()


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor():
    print("Poxa, você perdeu!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if (__name__ == "__main__"):
    jogar()
