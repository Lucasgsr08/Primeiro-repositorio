# construa um programa que realize um sorteio de um numero entre 1 e 20.
# o usuario tera 3 chances de acertar o numero.
# a cada tentativa o programa deve informar se o numero digitado é maior ou menor que o numero sorteado.
# o programa deve informar quantas tentativas foram necessárias para acertar o numero.
# o programa deve informar se o usuario ganhou ou perdeu.
# o programa deve perguntar se o usuario quer jogar novamente.
# o programa deve ser encerrado quando o usuario não quiser mais jogar.


import random
print("Bem-vindo ao jogo de adivinhação!")
print("Você tem 3 chances para adivinhar um número entre 1 e 20.")
while True:
    numero_sorteado = 10
    
    tentativas = 0
    ganhou = False

    while tentativas < 3:
        tentativa = int(input("Digite um número entre 1 e 20: "))
        tentativas += 1

        if tentativa < numero_sorteado:
            print("O número sorteado é maior.")
        elif tentativa > numero_sorteado:
            print("O número sorteado é menor.")
        else:
            ganhou = True
            break

    if ganhou:
        print(f"Parabéns! Você acertou o número {numero_sorteado} em {tentativas} tentativas.")
    else:
        print(f"Você perdeu! O número sorteado era {numero_sorteado}.")

    jogar_novamente = input("Você quer jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        break
print("Obrigado por jogar! Até a próxima.")
