import os

def jogar():
    
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")
    
#     palavra_secreta = 'banana'
#     enforcou = False
#     acertou = False

    palavra_secreta = "banana"
    letra_certa = ""
    tentativas = 0
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        
        entrada = input('Digite uma letra: ')
        tentativas += 1

        # Caso o usuario digitar mais uma letra
        if len(entrada) > 1:
            print("Digite apenas uma letra.")
            continue 
        
        #Adiciona a letra acertada a variavel letra_certa
        if entrada in palavra_secreta:
            letra_certa += entrada
        
        #Adiciona uma nova variavel para formar a palavra com base nos acertos
        palavra_formada = ''
        for letra in palavra_secreta:
            if letra in letra_certa:
                palavra_formada += letra
            else:
                palavra_formada += '*'
        print('Palavra formada:', palavra_formada)

        if palavra_formada == palavra_secreta:
            os.system('cls')
            print('VOCÊ GANHOU!! PARABÉNS!')
            print("A palavra era", palavra_secreta)
            print('Tentativas: ', tentativas)
            letra_certa = ""
            tentativas = 0

if __name__ == '__main__':
    jogar()