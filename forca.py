import random
import time
from colorama import init, Fore, Style #problema no colorama


init(autoreset=True)  # Inicializa o colorama

# Lista de palavras para o jogo da forca
palavras = ['python', 'programacao', 'desafio', 'computador', 'algoritmo']

# Estrutura de dados para representar a forca visualmente
forca_visual = [
    f'''
{Fore.GREEN}     +---+
     |   |
         |
         |
         |
         |
{Style.RESET_ALL}========''',
    f'''
{Fore.GREEN}     +---+
     O   |
         |
         |
         |
         |
{Style.RESET_ALL}========''',
    f'''
{Fore.GREEN}     +---+
     O   |
     |   |
         |
         |
         |
{Style.RESET_ALL}========''',
    f'''
{Fore.GREEN}     +---+
     O   |
    /|   |
         |
         |
         |
{Style.RESET_ALL}========''',
    f'''
{Fore.GREEN}     +---+
     O   |
    /|\\  |
         |
         |
         |
{Style.RESET_ALL}========''',
    f'''
{Fore.GREEN}     +---+
     O   |
    /|\\  |
    /    |
         |
         |
{Style.RESET_ALL}========''',
    f'''
{Fore.GREEN}     +---+
     O   |
    /|\\  |
    / \\  |
         |
         |
{Style.RESET_ALL}========'''
]


def escolher_palavra():
    # Escolhe aleatoriamente uma palavra da lista
    return random.choice(palavras)

def exibir_forca(tentativas):
    print(forca_visual[tentativas])
    print()

def exibir_palavra(palavra, letras_certas):
    for letra in palavra:
        if letra in letras_certas:
            print(Fore.GREEN + letra, end=' ')
        else:
            print('_', end=' ')
    print(Style.RESET_ALL)

def exibir_letras_erradas(letras_erradas):
    print(Fore.RED + 'Letras erradas:', end=' ')
    for letra in letras_erradas:
        print(letra, end=' ')
    print(Style.RESET_ALL)

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    tentativas = 0
    ganhou = False

    # mensagens de erro e acertos
    while True:

        # Limpar a tela
        print('\033c')

        # Exibir a forca e a palavra atual
        exibir_forca(tentativas)
        exibir_palavra(palavra, letras_certas)
        print()
        exibir_letras_erradas(letras_erradas)
        print()

        if ganhou == True:
            print("Parabéns, você acertou!")
            break
        # Solicitar uma nova letra ao jogador
        
        if len(letras_certas) < 4:
            letra = input('Digite uma letra: ').lower()
        else:
            pergunta = input('Você já sabe a resposta?').lower()
            if set(pergunta) == set(palavra):
                ganhou = True
                for i in pergunta:
                    if i in palavra and i not in letras_certas:
                        letras_certas.append(i)       
                    # continue 
            elif ganhou is not True:
                letra = input('Digite uma letra: ').lower()
        if ganhou is not True:
            if letra in letras_certas or letra in letras_erradas:
                print('Você já tentou essa letra. Tente novamente.')
                time.sleep(2)
            elif letra in palavra:
                letras_certas.append(letra)
                # Usando o construtor set() para criar um conjunto
                if set(letras_certas) == set(palavra):
                    print('Parabéns! Você venceu!')
                    break
            else:
                letras_erradas.append(letra)
                tentativas += 1  #tentativas = tentativas + 1
                if tentativas == len(forca_visual) - 1:
                    print(forca_visual[tentativas])
                    print(Fore.RED + 'Você perdeu! A palavra era',
                        palavra + Style.RESET_ALL)
                    break
        # Aguardar um pouco antes de continuar
        time.sleep(1)


# Inicia o jogo
jogar_forca()

