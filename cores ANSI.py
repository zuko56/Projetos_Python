'''\033[0;33;44m'''
'''style = 0, 1, 4, 7'''
'''text = 30 a 37'''
'''back = 40 a 47'''
print('\033[4;30mFON\033[m')
nome = input('Digite seu nome: ')
print('Bem vindo(a) {}{}{}'.format('\033[4;34m', nome, '\033[m'))