# Pesquisa binária em uma lista ordenada
def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista,3))

# Suponha que você tenha uma lsita com 128 nomes e esteja fazendo um pesquisa binária. Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?

# R: 7, pois log_2(128) = 7, pois 2^7 = 128

# Suponha que você duplique o tamanho da lista. Qual seria o número máximo de etapas agora?

# R: 8, pois log_2(256) = 8, pois 2^8 = 256 