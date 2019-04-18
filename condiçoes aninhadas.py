nome = str(input('Digite seu nome: ')).strip().lower()
if nome == 'guanabara':
    print('Curso em video')
elif nome == 'joão' or nome == 'maria' or nome == 'josé':
    print('Seu nome é popular no brasil')
elif nome in 'ana' or 'cláudia' or 'silva':
    print('Nomes femininos populares')
else:
    print('Fon')
print('Bom dia {}'.format(nome))
