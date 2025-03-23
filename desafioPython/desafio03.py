def contar_ocorrencias(strings):
    contador = {}  
    
    for string in strings:
        if string in contador:
            contador[string] += 1  
        else:
            contador[string] = 1  
    
    return contador

strings = ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']
resultado = contar_ocorrencias(strings)
print(resultado)
