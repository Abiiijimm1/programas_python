'''
Ejercicio7
Solicita al usuario ingresar un número N
y luego imprimir la suma de todos los números desde 1 hasta N
'''

numero = int(input('Ingresa un numero'))
suma = 0
i =1
while i <= numero:
    suma += i
    i += 1 
    
    print ('La suma es: ', suma)
