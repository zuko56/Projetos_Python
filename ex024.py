cidade = input('Digite o nome da cidade: ').strip()
comeco = cidade.upper().split()
print('Sua cidade começa com santo? {}'.format('SANTO' in comeco[0]))