import forca
import adivinhacao
import os


print("*********************************")
print("**Escolha o seu jogo!**")
print("*********************************")

print('[1] Forca'
      '\n[2] Adivinhação')

jogo = int(input('Qual jogo? '))

if jogo == 1:
    os.system('cls')
    print('Jogando jogo da Forca...')
    forca.jogar()
elif jogo == 2:
    os.system('cls')
    print('Jogando jogo da Adivinhação...')
    adivinhacao.jogar()
