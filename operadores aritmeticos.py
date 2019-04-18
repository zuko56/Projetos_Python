n1 = int(input('Digite o primeiro valor: '))
n2 = int(input("Digite o segundo valor: "))
print('A soma vale {}'.format(n1+n2))
print('A multiplicacao vale {}'.format(n1*n2))
print('A subtraçao vale {}'.format(n1-n2))
print('A divisao inteira vale {}'.format(n1//n2))
print('A divisao vale {:.3f}'.format(n1/n2)) # {:.3f} = definir as casas decimais que irão aparecer
print('O resto da divisao vale {}'.format(n1%n2))
print('A exponenciação vale {}'.format(n1**n2))
# end=' ' = junta os prints na mesma linha