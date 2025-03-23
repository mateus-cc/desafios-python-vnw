def calcular_media(dicionario):
    medias = []  
    
    for aluno, notas in dicionario.items():
        media = sum(notas) / len(notas)  
        medias.append((aluno, round(media, 2)))  
    
    return medias


notas_alunos = {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
resultado = calcular_media(notas_alunos)
print(resultado)

