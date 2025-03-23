def contar_palavras(texto):
    palavras = texto.split()  # Divide a string em palavras
    contador = {}  # Dicionário para armazenar as contagens
    
    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1  # Se a palavra já está no dicionário, incrementa a contagem
        else:
            contador[palavra] = 1  # Se não está no dicionário, adiciona com contagem 1
    
    return contador

# Testando a função
texto = "banana maçã banana laranja maçã maçã"
resultado = contar_palavras(texto)
print(resultado)
