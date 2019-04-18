num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
(1) para binário
(2) para octal
(3) para hexadecimal''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para binário será {}'.format(num, bin(num)[2:])) #[2:] = vai ler a segunda casa decimal pra frente, ignorando o 0b,0o,0h
elif opçao == 2:
    print('{} convertido para octal será {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para hexadecimal será {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, somente 1,2 ou 3')
