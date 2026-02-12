# =--- BIBLIOTECAS ---=

import random
import nltk
nltk.download('words')
from nltk.corpus import words #pip install nltk

import time
# -------------------------------------------------------

# =--- FUNÇÕES ---=

#Aqui através da dificuldade do jogo escolhida pelo usuário se obtem a quantidade de tentativas para acertar a palavra
def modo_Jogo(): 

    #while True para tratar os erros de escolha de seleção inexistente
    while True:
        try:
            print("Selecione a dificuldade do jogo: ")
            print("1 - Fácil")
            print("2 - Médio")
            print("3 - Difícil")
            print("4 - Insano")
            print("5 - Aleatório")
            opcao_modo_jogo = int(input(""))
        except ValueError:
            print("Por favor, digite um número inteiro!")

        if opcao_modo_jogo >= 1 and opcao_modo_jogo <= 5:
            break
        else:
            print("Selecione uma opção válida!")

    tentativas_por_usuario = -1
    dicas_por_dificuldade = -1

    match opcao_modo_jogo:

        case 1:
            tentativas_por_usuario = 6
            dicas_por_dificuldade = 3
            print(f"Você escolheu o modo Fácil, você terá {tentativas_por_usuario} tentativas para acertar a palavra!")
        case 2:
            tentativas_por_usuario = 4
            dicas_por_dificuldade = 2
            print(f"Você escolheu o modo Médio, você terá {tentativas_por_usuario} tentativas para acertar a palavra!")
        case 3:
            tentativas_por_usuario = 3
            dicas_por_dificuldade = 1
            print(f"Você escolheu o modo Difícil, você terá {tentativas_por_usuario} tentativas para acertar a palavra!")
        case 4:
            tentativas_por_usuario = 2
            dicas_por_dificuldade = 0
            print(f"Você escolheu o modo Insano, você terá {tentativas_por_usuario} tentativas para acertar a palavra!")
        case 5:
            lista_tentativa = [6, 4, 3, 2]
            tentativas_por_usuario = random.choice(lista_tentativa)

            lista_dicas_por_dificuldade = [3, 2, 1, 0]
            dicas_por_dificuldade = random.choice(lista_dicas_por_dificuldade)
            
            
            print(f"Você escolheu o modo Aleatório, você terá {tentativas_por_usuario} tentativas para acertar a palavra!")
    return [tentativas_por_usuario, dicas_por_dificuldade, opcao_modo_jogo]

#Função principal - seleciona a palavra da partida de acordo com o modo de jogo escolhido pelo usuário
def seleciona_Palavra_Partida(opcao_modo_jogo):

    lista_modo_facil = []
    lista_modo_medio = []
    lista_modo_dificil = [] 
    lista_modo_insano = []

    #Transferindo a biblioteca inteira para uma lista
    lista_palavras = words.words()

    #Separando a lista principal em listas de acordo com o tamanho da palavra
    for i in lista_palavras:
        if len(i) < 6:
            lista_modo_facil.append(i)
        elif len(i) >= 6 and len(i) < 8:
            lista_modo_medio.append(i)  
        elif len(i) >= 8 and len(i) < 10:
            lista_modo_dificil.append(i)
        elif len(i) <= 10:
            lista_modo_insano.append(i)

    match opcao_modo_jogo:
        case 1: #Caso das palavras do modo Fácil

            palavra_escolhida_computador = random.choice(lista_modo_facil)
            palavra_escolhida_computador = str(palavra_escolhida_computador.upper())   

        case 2: #Caso das palavras do modo Médio

            palavra_escolhida_computador = random.choice(lista_modo_medio)
            palavra_escolhida_computador = str(palavra_escolhida_computador.upper())

        case 3: #Caso das palavras do modo Difícil

            palavra_escolhida_computador = random.choice(lista_modo_dificil)
            palavra_escolhida_computador = str(palavra_escolhida_computador.upper())

        case 4: #Caso das palavras do modo Insano

            palavra_escolhida_computador = random.choice(lista_modo_insano)
            palavra_escolhida_computador = str(palavra_escolhida_computador.upper())

        case 5: #Caso das palavras do modo Aleatório

            escolha_lista = random.choice([lista_modo_facil, lista_modo_medio, lista_modo_dificil, lista_modo_insano])
            palavra_escolhida_computador = random.choice(escolha_lista)
            palavra_escolhida_computador = str(palavra_escolhida_computador.upper())

    return palavra_escolhida_computador

#Vai retornar True ou False - Caso retorne True, ele vai interromper o laço while
def adivinhar_Palavra_Inteira(palavra_usuario, palavra_computador):
    
    if palavra_usuario.upper() == palavra_computador.upper():
        print("Parabéns! Você acertou a palavra!")
        return True
    else:
        print("Você errou a palavra, tente novamente!")
        return False

def adivinhar_Letra_Palavra(letra_usuario, palavra_computador, palavra_atual_usuario):

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
    
    # Acrescenta a letra encontrada pelo usuário no vetor, p/ mostrar via terminal
    #Atualiza automaticamente a cada acerto refernte a letra do usuário
    if contador_letra_usuario > 0:    
        atualiza_Estado_Palavra(palavra_atual_usuario, palavra_computador, 1, letra_usuario)

    return

def cria_estado_Atual_Palavra(palavra_computador):

    palavra_atual_usuario = []

    for i in palavra_computador:
        palavra_atual_usuario.append("_")

    return palavra_atual_usuario

def atualiza_Estado_Palavra(palavra_atual_usuario, palavra_computador, opcao, letra_usuario):

    # Opção 0 - Apenas exibe a palavra ao usuário
    # Opção 1 - Atualiza a palavra com a letra que o usuário acertou

    #Caso mais simples - Apenas exibe a palavra ao usuário
    if opcao == 0:
        print(palavra_atual_usuario)
    else:
       
      indice = 0

      for indice, letra in enumerate(palavra_computador):
        if letra.upper() == letra_usuario.upper():
            palavra_atual_usuario[indice] = letra_usuario.upper()

    return

def Dicas(palavra_atual_usuario, palavra_computador): 

    while True:
        try:
            print("Selecione uma opção:")
            print("1 - Revelar letra dos extremos da palavra")
            print("2 - Revelar letra de uma posição aleatória da palavra")
            print("3 - Revelar letra de uma posição escolhida")
            print("4 - Revelar uma letra que não está na palavra")
            print("5 - Revelar uma letra que está na palavra")
            print("6 - Sair do menu de dicas")
            opcao_dica = int(input(""))
        except ValueError:
            print("Por favor, digite um número inteiro!")

        if opcao_dica >= 1 and opcao_dica <= 6:
            break
        else:
            print("Selecione uma opção válida!")

    tamanho_palavra = len(palavra_computador) #Escopo global da função
    tamanho_max_string = tamanho_palavra - 1 #Escopo global da função

    match opcao_dica:
        case 1:
            print("Você escolheu a opção 1 - 'Revelar letra dos extremos da palavra'")

            letra_extremo_esquerda = palavra_computador[0]
            letra_extremo_direita = palavra_computador[tamanho_max_string]

            #Atribuindo a letra á palavra no vetor
            palavra_atual_usuario[0] = letra_extremo_esquerda
            palavra_atual_usuario[tamanho_max_string] = letra_extremo_direita
            print(palavra_atual_usuario)
        case 2:
            print("Você escolheu a opção 2 - 'Revelar letra de uma posião aleatória da palavra'")

            #tamanho_palavra -1 pq apenas tamanho_palavra sai do range do index
            posicao_aleatoria = random.randint(0, (tamanho_max_string))
            letra_posicao_aleatoria = palavra_computador[posicao_aleatoria]

            #Atribuindo a letra á palavra no vetor
            palavra_atual_usuario[posicao_aleatoria] = letra_posicao_aleatoria
            print(palavra_atual_usuario)
        case 3:
            print("Você escolheu a opção 3 - 'Revelar letra de uma posição escolhida'")

            while True:
                posicao_escolhida = int(input("Digite a posição da letra que deseja descobrir: \n"))

                if posicao_escolhida >= 0 and posicao_escolhida <= tamanho_max_string:
                    break
                else:
                    print("Digite uma posição válida!")
            letra_ref_posicao_escolhida = palavra_computador[posicao_escolhida]

            #Atribuindo a letra á palavra no vetor
            palavra_atual_usuario[posicao_escolhida] = letra_ref_posicao_escolhida
            print(palavra_atual_usuario)
        case 4:
            print("Você escolheu a opção 4 - 'Revelar uma letra que não está na palavra'")

            #Descobrindo quais letras não estão na palavra escolhida pelo computador
            alfabeto = set("abcdefghijklmnopqrstuvwxyz")
            lista_letras_in_palavra_computador = set(palavra_computador)

            lista_letras_not_in_palavra_computador = list(alfabeto - lista_letras_in_palavra_computador)
            
            #Colocando o random para escolher uma letra da lista de letras que não estão na palavra e retorna essa letra para o usuário
            letra_sortida_not_in_palavra_computador = random.choice(lista_letras_not_in_palavra_computador)
            print(f"A letra {letra_sortida_not_in_palavra_computador} não está na palavra escolhida pelo computador!")
        case 5:
            print("Você escolheu a opção 5 - 'Revelar uma letra que está na palavra'")
            lista_letras_in_palavra_computador = list(set(palavra_computador)) #coloca numa lista para rodar o random

            #Colocando o random para escolher a letra
            letra_sortida_in_lista = random.choice(lista_letras_in_palavra_computador)
            print(letra_sortida_in_lista)
            print(f"A letra {letra_sortida_in_lista} está na palavra escolhida pelo computador!")
        case 6:
            print("Saindo do menu de dicas..")
    return

def Verifica_Palavra_Completa(palavra_atual_usuario):

    retorno = False

    for i in palavra_atual_usuario:
        if i == "_":
            retorno = True

    return retorno

#Calcula o tempo que o usuário levou na partida, p/ dps exibir p/ ele
def Calcula_Tempo_Jogada(tempo_inicio, tempo_fim):

    tempo_total_partida = tempo_fim - tempo_inicio
    tempo_horas = int(tempo_total_partida // 3600)
    tempo_minutos = int((tempo_total_partida % 3600) // 60)
    tempo_segundos = int(tempo_total_partida % 60)
    print(f"Sua partida levou {tempo_horas} horas, {tempo_minutos} minutos e {tempo_segundos} segundos!")

    return

def Inicializa_Jogo():

    partida = modo_Jogo()

    qtd_tentativas = partida[0]
    qtd_dicas = partida[1]
    opcao_modo_jogo = partida[2]

    palavra_escolhida_computador = seleciona_Palavra_Partida(opcao_modo_jogo)

    #APAGA ESSE PRINT DEPOIS QUE ESTIVER TUDO FUNCIONANDO !!!!!!!!!!!!!!!!!!!!!!!
    print(palavra_escolhida_computador) #APAGAR AQUI DEPOIS QUE FICAR PRONTO!!!!!!!!!!!!!!!!!!!

    acertou_palavra = False
    primeira_tentativa = True

    palavra_atual_usuario = cria_estado_Atual_Palavra(palavra_escolhida_computador)

    while qtd_tentativas != 0 or acertou_palavra == False:

        tempo_inicio = time.time()

        print("\n")

        if primeira_tentativa == True:
            print(palavra_atual_usuario)
        else:
            atualiza_Estado_Palavra(palavra_atual_usuario, palavra_escolhida_computador, 0, None)

        print("\n")

        #menu de opções
        while True:
            try:
                print("Selecione uma opção:")
                print("1 - Adivinhar a palavra")
                print("2 - Adivinhar a letra da palavra")
                print("3 - Sair do jogo")
                opcao_adivinhar_jogo = int(input(""))
                print("\n")
            except ValueError:
                print("Por favor, digite um número inteiro!")

            if opcao_adivinhar_jogo >= 1 and opcao_adivinhar_jogo <= 3:
                break
            else:
                print("Selecione uma opção válida")
        #Fecha while 

        #Chama as funções de adivinhar letra/palavra
        if opcao_adivinhar_jogo == 1:
            palavra_usuario = input("Digite a palavra que você acha que é: ")
            acertou_palavra = adivinhar_Palavra_Inteira(palavra_usuario, palavra_escolhida_computador)
        elif opcao_adivinhar_jogo == 2:
            letra_usuario = input("Digite a letra que você acha que está na palavra: ")
            adivinhar_Letra_Palavra(letra_usuario, palavra_escolhida_computador, palavra_atual_usuario)
        else:
            print("Saindo do jogo...")
            exit(1)

        #Caso o vetor de underscore estiver completo, has_underscore tem que interromper o laço while, considerando que a pessoa já acertou a palavra
        Has_Underscore = Verifica_Palavra_Completa(palavra_atual_usuario)

        #Se tiver underscore, a palavra ainda não foi revelada, se não tiver, o usuário já sabe a palavra toda
        if Has_Underscore == False:
            print("\n")
            atualiza_Estado_Palavra(palavra_atual_usuario, palavra_escolhida_computador, 0, None) #Mostra a lista completa pro usuário
            acertou_palavra = True
        

        #Interrompe o laço se o usuário acertar a palavra
        if acertou_palavra == True:
            tempo_fim = time.time()

            print("\n")
            if Has_Underscore == False:
                print("Parabéns, você completou a palavra!")
            else:
                print("Parabéns, você acertou a palavra!")
            Calcula_Tempo_Jogada(tempo_inicio, tempo_fim)
            break

        #Se não for a primeira tentativa do usuário e se ele tem dicas disponíveis, ele pode optar por receber dicas para facilitar o jogo
        if primeira_tentativa == False and qtd_dicas != 0:

            while True:
                print("\n")
                if qtd_dicas == 1:
                    print("Você tem apenas mais uma dica disponível, deseja utilizar ela?")
                else:
                    print(f"Você tem {qtd_dicas} dicas disponíveis, deseja utilizar uma?")

                try:
                    print("1 - Sim")
                    print("2 - Não")
                    opcao_utilizar_dicas = int(input("Selecione uma opção: \n"))
                except ValueError:
                    print("Por favor, digite um número inteiro!")
                
                if opcao_utilizar_dicas == 1 or opcao_utilizar_dicas == 2:
                    break
                else:
                    print("Por favor, selecione uma opção válida!")

            if opcao_utilizar_dicas == 1:
                Dicas(palavra_atual_usuario, palavra_escolhida_computador)
                qtd_dicas -= 1                

        #Alertar o usuário sobre a quantidade de tentativas que restam a ele
        qtd_tentativas -=  1
        
        if qtd_tentativas == 0:

            print("Suas tentativas acabaram! Você perdeu o jogo!")
            print(f"A palavra correta era: {palavra_escolhida_computador}")
            tempo_fim = time.time()
            Calcula_Tempo_Jogada(tempo_inicio, tempo_fim)

            break
        elif qtd_tentativas > 1: 
            print(f"Você tem {qtd_tentativas} tentativas restantes! ")
        else:
            print(f"Você tem {qtd_tentativas} tentativa restante!")

        primeira_tentativa = False

    #fecha while principal


# -------------------------------------------------------

# =-- AVISOS --=
"""
implementar o front-end (Gustavo)
"""


# =-- MAIN --=

if __name__ == "__main__":
    Inicializa_Jogo()

        
    
