# frase = 'Curso em Video Python' = atribuição de uma string a uma variavel

# toda string vai para a memória do computador e elas são guardadas caractere por caractere que também são chamados de indices,
# numeros sequenciais de zero a infinito, espaços também contam como caracteres

# fatiamento = frase[9] = 'V', usando a frase 'Curso em Video Python' como referencia

# frase[9:13] = começa no 9 e vai até o 13, porém o fim é sempre subtraido por 1 então vai até o 12 'Vide'

# frase[9:21] = vai do 9 ao 20, mesmo que não tenha o caractere 21 ele irá ser ignorado

# frase[9:21:2] = vai do 9 ao 20 porém pulando os caracteres de 2 em 2 'VdoPto'

# frase[:5] = o inicio não está determinado então sempre terá começo no zero e irá até 4 'Curso'

# frase[15:] = o final não está determinado então irá do 15 até o ultimo caractere existente 'Python'

# frase[9::3] = vai começar no 9 porém não tem fim determinado então irá ate o caractere final 'Video Python',
# depois disso será contado do 9 mas agora irá pular de 3 em 3 'VePh'

# Análise = len(frase) = irá mostrar o comprimento da string '21'

# frase.count('o') = irá contar quantas vezes tem o caractere 'o' na frase
# frase.count('o',0,13) = irá considerar do 0 ao 12 e irá contar quantas vezes tem o caractere 'o'

# frase.find('deo') = irá mostrar onde começou a determinada string, nesse caso será na posição '11'
# frase.find('Android') = essa string não tem dentro da frase analisada então será mostrado '-1', então significa -1 que não foi encontrado

# 'curso' in frase = irá verificar se existe tal string dentro da frase, então o resultado será 'true'

# Transformação = frase.replace('Python', 'Android') = irá procurar a string 'Python' e irá substituir por 'Android'

# frase.upper() = tudo o que for minusculo ficara em maisculo
# frase.lower() = transforma tudo em minusculo
# frase.capitalize() = a primeira letra da frase ficara em maiusculo
# e as primeiras letras das outras palavras serão minusculas 'Curso em video python'

# frase.title() = a primeira letra de todas as palavras ficarão em maiusculo 'Curso Em Video Python'
# frase.strip() = irá remover todos os espaços inuteis no inicio e fim da string ex: '   Aprenda Python  ' , 'Aprenda Python'
# frase.rstrip() = irá remover todos os espaços inuteis da direta
# frase.lstrip() = irá remover todos os espaços inuteis da esquerda

# Divisão = frase.split() = os espaços serão tratados como divisão, gera uma lista com todas as palavras divididas
# 'Curso' 'em' 'Video' 'Python'

#'-'.join(frase) = irá juntar a frase removendo as divisões e substituindo por '-' 'Curso-em-Video-Python'

# para printar um texto grande basta usar print('''...''')

frase = 'Curso em Video Python'
frase = frase.replace('Python', 'free')
print(frase)

