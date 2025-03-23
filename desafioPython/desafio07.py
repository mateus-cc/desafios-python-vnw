from collections import Counter

def frequentes(lista):
    frequencias = Counter(lista)
    
    mais_frequentes = sorted(frequencias, key=lambda x: (-frequencias[x], x))
    
    return mais_frequentes[:3]

lista = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
print(frequentes(lista))  
