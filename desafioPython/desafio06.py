d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}

dicionario_soma = {}

for chave in set(d1) | set(d2):  
    dicionario_soma[chave] = d1.get(chave, 0) + d2.get(chave, 0)

print(dicionario_soma) 