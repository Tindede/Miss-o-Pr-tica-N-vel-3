dicionario =  {
    1: {
        'nome': 'Maria',
        'idade': 26,
        'nacionalidade': 'brasileira'
    }
}

dicionario.update({
    2: {
        'nome': 'João',
        'idade': 30,
        'nacionalidade': 'brasileira'
    },
    3: {
        'nome': 'Ana',
        'idade': 22,
        'nacionalidade': 'portuguesa'
    }
})

print(dicionario)

dicionario_copia = dicionario.copy()

valor_removido = dicionario.pop(1)
print(valor_removido)

ultimo_elemento = dicionario.popitem()
print(ultimo_elemento)

dicionario.clear()
dicionario_copia.clear()

chaves = ['a', 'b', 'c']
novo_dicionario = dict.fromkeys(chaves, 'Valor padrão')

print(novo_dicionario.items())

print(novo_dicionario.keys())

print(novo_dicionario.values())



                 