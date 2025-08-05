
import random
import nltk
import winsound
nltk.download('words')
from nltk.corpus import words

lista_palavras = words.words()
escolha_computador = random.choice(lista_palavras)
escolha_computador = escolha_computador.lower()

import pyfiglet #pip install pyfiglet

def tutorial():

    print("\n")
    print("O jogo funciona da seguinte maneira")
    print("O computador vai escolher uma palavra totalmente aleatória do dicionário inglês")
    print("Seu objetivo é adivinhar essa palavra através de letras que você pode ir adivinhando conforme joga")
    print("Além de poder obter dicas da palavra enquanto joga")
    print(pyfiglet.figlet_format("Bom jogo!", font="slant"))

#fecha função tutorial

def advinhar_primeira(tentativa_jogador):

    print("\n")
    if(tentativa_jogador == 0):
        tentativa_jogador = 1

        tentativa_palavra = input("Digite a palavra que o computador escreveu:")
        tentativa_palavra = tentativa_palavra.lower()

        if(tentativa_palavra == escolha_computador):
            usuario_acerto_palavra = 1
            return usuario_acerto_palavra
        else:
            usuario_acerto_palavra = 0
            return usuario_acerto_palavra
    else:
        winsound.Beep(800, 600)
        print("\033[31mVocê não pode mais tentar essa opção!\033[0m")
#fecha função de adivinhar de primeira

def mostrar_letra_palavra():

    print("\n")
    contador_letra = 0

    print("\033[31m Por favor, digite apenas 1 letra por vez! \033[0m")
    tentativa_letra = input("Digite a letra que você acha que tem na palavra escolhida pelo computador: ")
    tentativa_letra = tentativa_letra.lower()

    tamanho_palavra = len(escolha_computador)

    i = 0
    while i< tamanho_palavra:

        palavra = escolha_computador[i]
        if(palavra == tentativa_letra):
            contador_letra += 1
        i += 1
    #fecha while

    if(contador_letra == 0):
        print(f"\033[31m A letra {tentativa_letra} não está na palavra escolhida pelo computador! \033[0m")
    elif(contador_letra == 1):
        print(f"\033[33m A letra {tentativa_letra} está na palavra escolhida pelo computador, e aparece {contador_letra} vez! \033[0m")
    elif(contador_letra >1):
        print(f"\033[32m A letra {tentativa_letra} está na palavra escolhida pelo computador, e aparece {contador_letra} vezes! \033[0m")

#fecha função de adivinhar a letra

def adivinhar_palavra_infinito():

    print("\n")
    tentativa_palavra_infinita = input("Digite a palavra escolhida pelo computador:")

    if(tentativa_palavra_infinita == escolha_computador):
        usuario_acerto_palavra = 1
        return usuario_acerto_palavra
    else:
        usuario_acerto_palavra = 0
        return usuario_acerto_palavra
#fecha função
        
def dicas(dicas_disponiveis):

    print("\n")
    if(dicas_disponiveis == 1):
        print("\033[31m Você tem apenas 1 dica disponível \033[0m")
    elif(dicas_disponiveis == 2):
        print("\033[33m Você tem 2 dicas disponíveis! \033[0m")

    if(dicas_disponiveis == 1 or dicas_disponiveis == 2):

        while True:
        
            print("\033[36m 1 \033[0m"" - Total de letras da palavra")
            print("\033[36m 2 \033[0m"" - Mostrar a letra inicial")
            print("\033[36m 3 \033[0m"" - Mostrar a letra final")
            print("\033[36m 4 \033[0m"" - Mostrar a letra de uma posição de escolha do usuário")
            opcao_dica = int(input("Digite a opção da dica que deseja obter:"))

            if(opcao_dica >=1 and opcao_dica <=4):
                break
            else:
                winsound.Beep(800, 600)
                print("\033[31m Por favor, escolha uma opção válida! \033[0m")
        #fecha while

        if(opcao_dica == 1):
            
            total_letras_palavra = len(escolha_computador)
            print(f"A palavra escolhida pelo computador tem {total_letras_palavra} letras!")
            dicas_disponiveis = dicas_disponiveis - 1
            return dicas_disponiveis
        
        elif(opcao_dica == 2):

            print(f"A primeira letra da palavra escolhida pelo computador é: '{escolha_computador[0]}'")
            dicas_disponiveis = dicas_disponiveis - 1
            return dicas_disponiveis
        
        elif(opcao_dica == 3):

            
            auxiliar = len(escolha_computador)
            print(f"A última letra da palavra escolhida pelo computador é: '{escolha_computador[auxiliar-1]}'")
            dicas_disponiveis = dicas_disponiveis - 1
            return dicas_disponiveis

        else:

            while True:
                posicao = int(input(f"Digite um número referente á posição da letra da palavra que deseja descobrir: (válido de 0 á {auxiliar - 1})"))

                if(posicao >= 0 and posicao <=(auxiliar -1)):
                    break
                else:
                    winsound.Beep(800, 600)
                    print("\033[31m Por favor, digite uma posição válida de acordo com a quantidade de letras que existem na palavra! \033[0m")
            #fecha while
            print(f"A letra da posição {posicao} da palavra escolhida pelo computador é: '{escolha_computador[posicao]}'")
            dicas_disponiveis = dicas_disponiveis - 1
            return dicas_disponiveis
        #fecha else
    else:
        print("\033[31m Suas dicas disponíveis já acabaram! \033[0m")
    

#fecha função dicas

primeiro_acesso = bool(True)
usuario_acerto_palavra = 0

contador_tentativas = 0

tentativa_jogador = 0

contador_dicas = 2

while True:

    contador_tentativas += 1

   
    if(primeiro_acesso == True):
        primeiro_acesso = False #reatribui o valor p/ na próxima entrar na segunda tentativa do jogador

        while True:
            print(pyfiglet.figlet_format("Bem-vindo(a) ao jogo de adivinhar a palavra!", font="slant"))
            print("Deseja saber como funciona?")
            print("\033[36m 1 \033[0m - Sim")
            print("\033[36m 2 \033[0m - Não")
            opcao_tutorial = int(input("Digite sua opção:"))

            if(opcao_tutorial == 1 or opcao_tutorial == 2):
                break
            else:
                winsound.Beep(800, 600)
                print("\033[31m Por favor, escolha uma opção válida! \033[0m")
        #fecha while

        if(opcao_tutorial == 1):
            print("\033[36m Iniciando o tutorial... \033[0m")
            tutorial()

            print("\033[36m Iniciando o jogo... \033[0m")
            print("\n")
            while True:
                print("Para começar o jogo, escolha uma opção:")
                print("\033[36m 1 \033[0m"" - Adivinhar a palavra diretamente (válido apenas 1 vez)")
                print("\033[36m 2 \033[0m"" - Adivinhar as letras para conseguir adivinhar a palavra (válido infinitas vezes)")
                opcao_jogo = int(input("Digite sua opção:"))

                if(opcao_jogo == 1 or opcao_jogo == 2):
                    break
                else:
                    winsound.Beep(800, 600)
                    print("\033[31m Por favor, escolha uma opção válida! \033[0m")
            #fecha while

            if(opcao_jogo == 1):

                print("\033[31m Nesta opção você tem apenas 1 tentativa! \033[0m") 
                usuario_acerto_palavra = advinhar_primeira(tentativa_jogador)

                if(usuario_acerto_palavra == 1):

                    
                    print("\033[32m Parabéns, você acertou a palavra que o computador escolheu! na primeira tentativa! \033[0m")
                    break
                else:
                    print("\033[31m Infelizmente, você errou a palavra que o computador escolheu! Continue tentando.. \033[0m")
            else:

                mostrar_letra_palavra()              
        else:
            print("\033[36m Iniciando o jogo... \033[0m")

            print("\n")
            while True:
                print("Para começar o jogo, escolha uma opção:")
                print("\033[36m 1 \033[0m"" - Adivinhar a palavra diretamente (válido apenas 1 vez, somente neste momento)")
                print("\033[36m 2 \033[0m"" - Adivinhar as letras para conseguir adivinhar a palavra (válido infinitas vezes)")
                opcao_jogo = int(input("Digite sua opção:"))

                if(opcao_jogo == 1 or opcao_jogo == 2):
                    break
                else:
                    winsound.Beep(800, 600)
                    print("\033[31m Por favor, escolha uma opção válida! \033[0m")
            #fecha while

            if(opcao_jogo == 1):

                print("\033[31m Nesta opção você tem apenas 1 tentativa! \033[0m") 
                usuario_acerto_palavra = advinhar_primeira(tentativa_jogador)

                if(usuario_acerto_palavra == 1):

                    if(contador_tentativas == 1):
                        print(f"\033[32m Parabéns, você acertou a palavra que o computador escolheu! tendo feito apenas {contador_tentativas} tentativa \033[0m")
                        break
                    else:
                        print(f"\033[32m Parabéns, você acertou a palavra que o computador escolheu! tendo feito {contador_tentativas} tentativas \033[0m")
                        break

                else:
                    print("\033[31m Infelizmente, você errou a palavra que o computador escolheu! Continue tentando.. \033[0m")
            else:

                mostrar_letra_palavra()

        #fecha else do 1o acesso
    else:
        #caso de não ser a primeira adivinhação do jogador
        print("\n")
        while True:
            print("Deseja continuar tentando?")
            print("\033[36m 1 \033[0m"" - Sim")
            print("\033[36m 2 \033[0m"" - Não")
            opcao_continuar_jogo = int(input("Digite sua opção:"))

            if(opcao_continuar_jogo == 1 or opcao_continuar_jogo == 2):
                break
            else:
                winsound.Beep(800, 600)
                print("\033[31m Por favor, escolha uma opção válida! \033[0m")
        #fecha while

        if(opcao_continuar_jogo == 1):

            if(contador_tentativas >= 3 and (contador_dicas == 1 or contador_dicas == 2)):

                print("\n")
                while True:
                    print("Deseja obter uma dica?")
                    print("\033[36m 1 \033[0m"" - Sim")
                    print("\033[36m 2 \033[0m"" - Não")
                    opcao_dica = int(input("Digite sua opção:"))

                    if(opcao_dica == 1 or opcao_dica == 2):
                        break
                    else:
                        winsound.Beep(800, 600)
                        print("\033[31m Por favor, escolha uma opção válida! \033[0m")
                #fecha while

                if(opcao_dica == 1):

                    contador_dicas = dicas(contador_dicas)

                else:
                    print(f"\033[32m Caso queira utilizar, você ainda têm {contador_dicas} dicas restantes! \033[0m")
            #fecha if dicas

            print("\n")
            while True:

                print("Escolha uma opção:")
                print("\033[36m 1 \033[0m"" - Adivinhar a letra")
                print("\033[36m 2 \033[0m"" - Adivinhar a palavra")
                opcao_menu_infinitas_tentativas = int(input("Digite sua opção:"))

                if(opcao_menu_infinitas_tentativas == 1 or opcao_menu_infinitas_tentativas == 2):
                    break
                else:
                    winsound.Beep(800, 600)
                    print("\033[31m Por favor, escolha uma opção válida! \033[0m")
            #fecha while

            if(opcao_menu_infinitas_tentativas == 1):
                mostrar_letra_palavra()
                
            else:
                usuario_acerto_palavra = adivinhar_palavra_infinito()

            if(usuario_acerto_palavra == 1 and opcao_menu_infinitas_tentativas == 2):
                print(f"\033[32m Parabéns, você acertou a palavra tendo feito {contador_tentativas} tentativas! \033[0m")
                break
            elif(usuario_acerto_palavra == 0 and opcao_menu_infinitas_tentativas == 2):
                print("\033[31m Infelizmente você errou a palavra que foi escolhida pelo computador! Continue tentando.. \033[0m")
        else:
            winsound.Beep(800, 600)
            if(contador_tentativas == 1):
                print(f"Durante o jogo, você fez {contador_tentativas} tentativa!")
            else:
                print(f"Durante o jogo, você fez {contador_tentativas} tentativas!")

            print(pyfiglet.figlet_format("Saindo do jogo...", font="slant"))
            break
        #fecha else
#fecha while principal


