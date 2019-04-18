nome = str(input('Digite seu nome: ')).strip() # retirar todos os espaços inuteis inicio e fim
dividido = nome.split()
print('Seu nome com todas as letras maiusculas: {}, minusculas: {}, quantas letras ao todo: {}, quantas letras tem o primeiro nome: {}'.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), len(dividido[0])))
# len(nome) - nome.count(' ') = vai retirar a contagem de todos os espaços existentes