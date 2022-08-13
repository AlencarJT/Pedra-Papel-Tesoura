from random import randint
from time import sleep

print('Olá, Bem-Vindo ao Pedra, Papel, Tesoura')
empate = 0
derrota = 0
vitoria = 0

print('Você deverá escolher uma das seguintes opções: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n Qualquer outra entrada finalizará o jogo')
print(f'Vamos iniciar')
print('-' * 20)

while True:
    print('\U0001F3B5')
    print('Pedra... \U0001F91B')
    sleep(1)
    print('Papel... \U0001F590')
    sleep (1)
    print('Tesoura!! \U0001F596')
    print('_' * 20)
    usuario = int(input('Digite o número referente a sua escolha: '))
    print('_' * 20)
    computador = randint(1, 3)
    if usuario == 1:
        sleep(1)
        print('Você escolheu PEDRA!')
        if computador == 1:
            sleep(1)
            print('Computador Jogou Pedra')
            print('Vocês dois escolheram PEDRA, EMPATE')
            empate += 1
        elif computador == 2:
            sleep(1)
            print('Computador Jogou Papel')
            print('PAPEL ganha da PEDRA, COMPUTADOR VENCEU')
            derrota += 1
        else:
            sleep(1)
            print('Computador Jogou Tesoura')
            print('TESOURA perde da PEDRA, VOCÊ VENCEU!')
            vitoria += 1
    elif usuario == 2:
        sleep(1)
        print('Você escolheu PAPEL')
        if computador == 1:
            sleep(1)
            print('Computador Jogou Pedra')
            print('PEDRA perde do PAPEL, VOCÊ VENCEU!')
            vitoria += 1
        elif computador == 2:
            sleep(1)
            print('Computador Jogou Papel')
            print('Vocês dois escolheram PAPEL, EMPATE')
            empate += 1
        else:
            sleep(1)
            print('Computador Jogou Tesoura')
            print('TESOURA ganha do PAPEL, COMPUTADOR VENCEU')
            derrota += 1
    elif usuario == 3:
        sleep(1)
        print('Você escolheu TESOURA')
        if computador == 1:
            sleep(1)
            print('Computador Jogou Pedra')
            print('PEDRA ganha da TESOURA, COMPUTADOR VENCEU')
            derrota += 1
        elif computador == 2:
            sleep(1)
            print('Computador Jogou Papel')
            print('PAPEL perde da TESOURA, VOCÊ VENCEU!')
            vitoria += 1
        else:
            sleep(1)
            print('Computador Jogou Tesoura')
            print('Vocês dois escolheram TESOURA, EMPATE')
            empate += 1
    else:
        print('Fim de jogo')
        print('-' * 40)
        sleep(1)
        print(f'Você GANHOU {vitoria} partidas')
        print(f'Você EMPATOU {empate} partidas')
        print(f'Você PERDEU {derrota} partidas')
        print('-' * 40)
        if derrota > vitoria:
            print('Você é muito ruim nesse jogo, QUE VERGONHA')
        break
    print('-' * 20)
sleep (1)
print('Jogo Finalizado, obrigado por participar')