num = int(input('Digite um valor: '))
c = num
f = 1
print('Cálculo de {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))
