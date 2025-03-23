def palindromo(palavra):
    return palavra == palavra[::-1]

entrada = "radar"
print(palindromo(entrada)) 
