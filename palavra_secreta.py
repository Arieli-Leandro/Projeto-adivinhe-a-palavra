# =--- BIBLIOTECAS ---=

import random
import nltk
import winsound
nltk.download('words')
from nltk.corpus import words #pip install nltk

import pyfiglet #pip install pyfiglet

import pygame #adicionar um som de fundo no final

# -------------------------------------------------------

# Random esconlhendo qual vai ser a palavra

lista_palavras = words.words()

palavra_escolhida_computador = random.choice(lista_palavras)
print(palavra_escolhida_computador)


# =--- FUNÇÕES ---=

#Aqui através da dificuldade do jogo escolhida pelo usuário se obtem a quantidade de tentativas para acertar a palavra
def modo_Jogo(): 

    #while True para tratar os erros de escolha de seleção inexistente
    while True:

        print("Selecione a dificuldade do jogo: ")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Difícil")
        print("4 - Insano")
        print("5 - Aleatório")
        opcao_modo_jogo = int(input())

        if opcao_modo_jogo >= 1 and opcao_modo_jogo <= 5:
            break
        else:
            print("Selecione uma opção válida!")

    tentativas_por_usuario = -1

    match opcao_modo_jogo:

        case 1:

            tentativas_por_usuario = 12
            print(f"Você escolheu o modo Fácil, você terá {tentativas_por_usuario} tentativas para acertar a palavra!")

        case 2:

            tentativas_por_usuario = 7
            print(f"Você escolheu o modo Médio, você terá {tentativas_por_usuario} tentativas para acertar a palavra!")


        case 3:

            tentativas_por_usuario = 5
            print(f"Você escolheu o modo Difícil, você terá {tentativas_por_usuario} tentativas para acertar a palavra!")

        case 4:

            tentativas_por_usuario = 2
            print(f"Você escolheu o modo Insano, você terá {tentativas_por_usuario} tentativas para acertar a palavra!")

        case 5:

            lista_tentativa = [12, 7, 5, 2]
            tentativas_por_usuario = random.choice(lista_tentativa)
            print(f"Você escolheu o modo Aleatório, você terá {tentativas_por_usuario} tentativas para acertar a palavra!")


    return tentativas_por_usuario


#Vai retornar True ou False - Caso retorne True, ele vai interromper o laço while
def adivinhar_Palavra_Inteira(palavra_usuario, palavra_computador):
    
    if palavra_usuario.upper() == palavra_computador.upper():
        return True
    else:
        print("Você errou a palavra, tente novamente!")
        return False



def adivinhar_Letra_Palavra(letra_usuario, palavra_computador):

    contador_letra_usuario = 0

    for i in palavra_computador:
        if i.upper() == letra_usuario.upper():
            contador_letra_usuario += 1

    if contador_letra_usuario == 0:
        print(f"A letra '{letra_usuario}' não está na palavra escolhida pelo computador!")
    elif contador_letra_usuario == 1:
        print(f"Há apenas 1 letra '{letra_usuario}' na palavra escolhida pelo computador!")
    else:
        print(f"Há {contador_letra_usuario} letras '{letra_usuario}' na palavra escolhida pelo computador!")
    
    return

# -------------------------------------------------------

# =-- AVISOS --=
"""
implementar a função de adivinhar letra da palavra
implementar as dicas
implementar o som de fundo
implementar o front-end

"""


# =-- MAIN --=

qtd_tentativas = modo_Jogo()

acertou_palavra = False

while qtd_tentativas != 0 or acertou_palavra == False:
    
    while True:

        print("Selecione uma opção:")
        print("1 - Adivinhar a palavra")
        print("2 - Adivinhar a letra da palavra")
        opcao_adivinhar_jogo = int(input(""))

        if opcao_adivinhar_jogo == 1 or opcao_adivinhar_jogo == 2:
            break
        else:
            print("Selecione uma opção válida")
    #Fecha while 

    if opcao_adivinhar_jogo == 1:
        palavra_usuario = input("Digite a palavra que você acha que é: ")
        acertou_palavra = adivinhar_Palavra_Inteira(palavra_usuario, palavra_escolhida_computador)
    else:
        letra_usuario = input("Digite a letra que você acha que está na palavra: ")
        adivinhar_Letra_Palavra(letra_usuario, palavra_escolhida_computador)

    #Interrompe o laço se o usuário acertar a palavra
    if acertou_palavra == True:
        print("Parabéns! Você acertou a palavra!")
        break

    #Alertar o usuário sobre a quantidade de tentativas que restam a ele
    qtd_tentativas = qtd_tentativas - 1
    
    if qtd_tentativas > 1:
        print(f"Você tem {qtd_tentativas} tentativas restantes! ")
    else:
        print(f"Você tem {qtd_tentativas} tentativa restante!")
        
        
    
