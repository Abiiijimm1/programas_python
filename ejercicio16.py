'''
Filtrar numeros pares de una lista utilizando filter
'''
numeros = [1,2,3,4,5,6,7,8]

pares = list(filter(lambda x:x%2==0, numeros))

print(numeros)
print(pares)
