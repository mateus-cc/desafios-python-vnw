numeros = [2,4,10,3,9,7,15,22]

def somarPares():
    soma = 0
    for numero in numeros:
          if numero % 2 == 0:
               soma += numero
    return soma


print(somarPares())




