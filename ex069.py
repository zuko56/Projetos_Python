print('C a d a s t r o')
print('=' * 20)
contmaior = conthomem = contmulher = 0
while True:
    print('Cadastre uma pessoa')
    print('=' * 20)
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        contmaior += 1
    print('=' * 20)
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and idade < 20:
        contmulher += 1
    print('=' * 20)
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    perg = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]: ')).strip().upper()
    print('=' * 20)
    if perg == 'N':
        break
print(f'Maior de 18 anos são {contmaior} pessoas')
print(f'Foram cadastrados {conthomem} homem(s)')
print(f'Foram cadastradas {contmulher} mulher(s) com menos de 20 anos')
