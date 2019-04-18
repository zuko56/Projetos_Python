from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
ope = 0
while ope != 5:
    print('''Aperte      [1] somar
            [2] multiplicar
            [3] maior
            [4] novos números
            [5] sair do programa''')
    ope = int(input('Digite a operação: '))
    if ope == 1:
        soma = num1 + num2
        print('A soma de {} + {} é {}'.format(num1, num2, soma))
    elif ope == 2:
        mult = num1 * num2
        print('A multiplicação de {} X {} é {}'.format(num1, num2, mult))
    elif ope == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior é {}'.format(num1, num2, maior))
    elif ope == 4:
        print('Digite novos números')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif ope == 5:
        print('Saindo do programa...')
        sleep(1)
        break
    else:
        print('Opção inválida, tente novamente')
    print('=' * 35)
print('Fim do Programa')
