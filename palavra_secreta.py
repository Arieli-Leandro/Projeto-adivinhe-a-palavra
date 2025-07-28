import random
import nltk
import winsound
nltk.download('words')
from nltk.corpus import words

lista_palavras = words.words()
escolha_computador = random.choice(lista_palavras)
escolha_computador = escolha_computador.lower()
print(escolha_computador)

def tutorial():

    print("O jogo funciona da seguinte maneira")
    print("O computador vai escolher uma palavra totalmente aleatória do dicionário inglês")
    print("Seu objetivo é adivinhar essa palavra através de letras que você pode ir adivinhando conforme joga")
    print("Além de poder obter dicas da palavra enquanto joga")
    print("Bom jogo!")
#fecha função tutorial

def advinhar_primeira(tentativa_jogador):

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
        print("Você não pode mais tentar essa opção!")
#fecha função de adivinhar de primeira

def mostrar_letra_palavra():

    contador_letra = 0

    print("Por favor, digite apenas 1 letra por vez!")
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
        print(f"A letra {tentativa_letra} não está na palavra escolhida pelo computador!")
    elif(contador_letra == 1):
        print(f"A letra {tentativa_letra} está na palavra escolhida pelo computador, e aparece {contador_letra} vez!")
    elif(contador_letra >1):
        print(f"A letra {tentativa_letra} está na palavra escolhida pelo computador, e aparece {contador_letra} vezes!")

#fecha função de adivinhar a letra

def adivinhar_palavra_infinito():

    tentativa_palavra_infinita = input("Digite a palavra escolhida pelo computador:")

    if(tentativa_palavra_infinita == escolha_computador):
        usuario_acerto_palavra = 1
        return usuario_acerto_palavra
    else:
        usuario_acerto_palavra = 0
        return usuario_acerto_palavra
#fecha função
        
def dicas(dicas_disponiveis):

    #As dicas vão aparecer somente depois de 3 tentativas de acerto da palavra

    print("Você pode apenas obter duas dicas!")
    print(f"Dicas disponíveis para o usuário: {dicas_disponiveis}")

    if(dicas_disponiveis == 1 or dicas_disponiveis == 2):

        while True:
        
            print("1 - Total de letras da palavra")
            print("2 - Mostrar a letra inicial")
            print("3 - Mostrar a letra final")
            print("4 - Mostrar a letra de uma posição de escolha do usuário")
            opcao_dica = int(input("Digite a opção da dica que deseja obter:"))

            if(opcao_dica >=1 and opcao_dica <=4):
                break
            else:
                winsound.Beep(800, 600)
                print("Por favor, escolha uma opção válida!")
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
                    print("Por favor, digite uma posição válida!")
            #fecha while
            print(f"A letra da posição {posicao} da palavra escolhida pelo computador é: '{escolha_computador[posicao]}'")
            dicas_disponiveis = dicas_disponiveis - 1
            return dicas_disponiveis
        #fecha else
    else:
        print("Suas dicas disponíveis já acabaram!")
    

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
            print("Bem-vindo(a) ao jogo de adivinhar a palavra!")
            print("Deseja saber como funciona?")
            print("1 - Sim")
            print("2 - Não")
            opcao_tutorial = int(input("Digite sua opção:"))

            if(opcao_tutorial == 1 or opcao_tutorial == 2):
                break
            else:
                winsound.Beep(800, 600)
                print("Por favor, escolha uma opção válida!")
        #fecha while

        if(opcao_tutorial == 1):
            print("Iniciando o tutorial...")
            tutorial()

            print("Iniciando o jogo...")

            while True:
                print("Para começar o jogo, escolha uma opção:")
                print("1 - Adivinhar a palavra diretamente (válido apenas 1 vez)")
                print("2 - Adivinhar as letras para conseguir adivinhar a palavra (válido infinitas vezes)")
                opcao_jogo = int(input("Digite sua opção:"))

                if(opcao_jogo == 1 or opcao_jogo == 2):
                    break
                else:
                    winsound.Beep(800, 600)
                    print("Por favor, escolha uma opção válida!")
            #fecha while

            if(opcao_jogo == 1):

                print("Nesta opção você tem apenas 1 tentativa!")
                usuario_acerto_palavra = advinhar_primeira(tentativa_jogador)

                if(usuario_acerto_palavra == 1):

                    
                    print("Parabéns, você acertou a palavra que o computador escolheu! na primeira tentativa!")
                    break
                else:
                    print("Infelizmente, você errou a palavra que o computador escolheu! Continue tentando..")
            else:

                mostrar_letra_palavra()              
        else:
            print("Iniciando o jogo...")

            while True:
                print("Para começar o jogo, escolha uma opção:")
                print("1 - Adivinhar a palavra diretamente (válido apenas 1 vez, somente neste momento)")
                print("2 - Adivinhar as letras para conseguir adivinhar a palavra (válido infinitas vezes)")
                opcao_jogo = int(input("Digite sua opção:"))

                if(opcao_jogo == 1 or opcao_jogo == 2):
                    break
                else:
                    winsound.Beep(800, 600)
                    print("Por favor, escolha uma opção válida!")
            #fecha while

            if(opcao_jogo == 1):

                print("Nesta opção você tem apenas 1 tentativa!")
                usuario_acerto_palavra = advinhar_primeira(tentativa_jogador)

                if(usuario_acerto_palavra == 1):

                    if(contador_tentativas == 1):
                        print(f"Parabéns, você acertou a palavra que o computador escolheu! tendo feito apenas {contador_tentativas} tentativa")
                        break
                    else:
                        print(f"Parabéns, você acertou a palavra que o computador escolheu! tendo feito {contador_tentativas} tentativas")
                        break

                else:
                    print("Infelizmente, você errou a palavra que o computador escolheu! Continue tentando..")
            else:

                mostrar_letra_palavra()

        #fecha else do 1o acesso
    else:
        #caso de não ser a primeira adivinhação do jogador
        while True:
            print("Deseja continuar tentando?")
            print("1 - Sim")
            print("2 - Não")
            opcao_continuar_jogo = int(input("Digite sua opção:"))

            if(opcao_continuar_jogo == 1 or opcao_continuar_jogo == 2):
                break
            else:
                winsound.Beep(800, 600)
                print("Por favor, escolha uma opção válida!")
        #fecha while

        if(opcao_continuar_jogo == 1):

            if(contador_tentativas >= 3 and (contador_dicas == 1 or contador_dicas == 2)):

                while True:
                    print("Deseja obter uma dica?")
                    print("1 - Sim")
                    print("2 - Não")
                    opcao_dica = int(input("Digite sua opção:"))

                    if(opcao_dica == 1 or opcao_dica == 2):
                        break
                    else:
                        winsound.Beep(800, 600)
                        print("Por favor, escolha uma opção válida!")
                #fecha while

                if(opcao_dica == 1):

                    contador_dicas = dicas(contador_dicas)

                else:
                    print(f"Caso queira utilizar, você ainda têm {contador_dicas} dicas restantes!")
            #fecha if dicas

            while True:

                print("Escolha uma opção:")
                print("1 - Adivinhar a letra")
                print("2 - Adivinhar a palavra")
                opcao_menu_infinitas_tentativas = int(input("Digite sua opção:"))

                if(opcao_menu_infinitas_tentativas == 1 or opcao_menu_infinitas_tentativas == 2):
                    break
                else:
                    winsound.Beep(800, 600)
                    print("Por favor, escolha uma opção válida!")
            #fecha while

            if(opcao_menu_infinitas_tentativas == 1):
                mostrar_letra_palavra()
                
            else:
                usuario_acerto_palavra = adivinhar_palavra_infinito()

            if(usuario_acerto_palavra == 1 and opcao_menu_infinitas_tentativas == 2):
                print(f"Parabéns, você acertou a palavra tendo feito {contador_tentativas} tentativas!")
                break
            elif(usuario_acerto_palavra == 0 and opcao_menu_infinitas_tentativas == 2):
                print("Infelizmente você errou a palavra que foi escolhida pelo computador! Continue tentando..")
        else:
            winsound.Beep(800, 600)
            print("Saindo do jogo...")
            break
        #fecha else
#fecha while principal


