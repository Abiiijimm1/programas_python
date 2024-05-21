'''
Ejercicio 14
Contar el número de vocales en una lista de palabras utilizando map
'''
def contar (palabra):
   return sum (1 for letra in palabra if letra.lower() in 'aeiou')
    
palabras = ['Hola', 'mundo', 'python']

conteos = list (map (contar, palabras))
print (palabras)
print (conteos)
