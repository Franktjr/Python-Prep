#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:
def primo(numero):
    resultado = [x for x in range(1,numero+1) if numero % x == 0]
    cantidad_divisibles = len(resultado)

    if cantidad_divisibles == 2:
        return True
    else:
        return False

intentos = 0
while intentos < 3:
    numero_calcular = input('Igrese un número entero positivo: ')
    if numero_calcular.isdigit():
        numero_calcular = int(numero_calcular)
        resultado_primo = primo(numero_calcular)
        print(resultado_primo)
        break
    else:
        print('No ha ingresado un número entero positivo.')
    intentos+=1
    if intentos == 3:
        print('Ha agotados sus intentos')

print("Ha salido de la funcion exitosamente")




# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
def primo(numero):
    resultado = [x for x in range(1,numero+1) if numero % x == 0]
    cantidad_divisibles = len(resultado)

    if cantidad_divisibles == 2:
        return True
    else:
        return False

lista_numeros = [2,5,6,8,7,9,3]
lista_primos = list(filter(lambda x: primo(x),lista_numeros))
print('lista_primos',lista_primos)




# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
def numero_mas_repetido(lista):
    frecuencia = {}
    
    for numero in lista:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    
    mas_repetido = max(frecuencia, key=frecuencia.get)#especificamos que busque el maximo entre los valores de cada clave del diciconario, key=frecuencia.get es como una condicion de donde teine que buscar, pero al final me devuelve es la clave con el valor mas alto
    print('mas_repetido',mas_repetido)
    repeticiones = frecuencia[mas_repetido]# com en mas_repetido se guarda la clave oc el valor mas alto, entonces aqui guardamos el valor de esa clave. y asi tendriamos dos variable suna cn clave y otra  con el valor.
    print('repeticiones',repeticiones)
    
    return mas_repetido, repeticiones

numeros = [7,3,2,5,3,7,3,5,9,7,7,3,7,5,3]
resultado = numero_mas_repetido(numeros)
print(f"El número más repetido es {resultado[0]} y se repite {resultado[1]} veces.")




# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def llamando_operacion(medida_origen,valor,medida_destino):

    if medida_origen == 'F' and medida_destino == 'K':
        resultado = ((valor-32)/1.8) + 273.15
    elif medida_origen == 'F' and medida_destino == 'C':
        resultado =  (valor-32)/1.8
    elif medida_origen == 'C' and medida_destino == 'K':
        resultado = valor + 273.15
    elif medida_origen == 'C' and medida_destino == 'F':
        resultado = (valor * 1.8) + 32 #1.8 es lo mismo que 9/5
    elif medida_origen == 'K' and medida_destino == 'F':
        resultado = ((valor-273.15) * 1.8) + 32
    elif medida_origen == 'K' and medida_destino == 'C':
        resultado = valor - 273.15
    
    cadena = f'{resultado}°{medida_destino}'
    return cadena 

intentos_medida = 0
while intentos_medida < 3:
    print('Ingrese la medida de origen del valor a convertir:')
    print('Para °F escriba "F" sin comillas')
    print('Para °K escriba "K" sin comillas')
    print('Para °C escriba "C" sin comillas')
    medida_origen = input().upper()# en caso de ingrreesar misnucula, esta se tome como valida

    opciones = ['F','K','C']
    if medida_origen in opciones:
        intentos_medida = 0
        while intentos_medida < 3:
            print('Ingrese la medida de destino del valor a convertir:')
            print('Para °F escriba "F" sin comillas')
            print('Para °K escriba "K" sin comillas')
            print('Para °C escriba "C" sin comillas')
            medida_destino = input().upper()# en caso de ingrresar misnucula, esta se tome como valida

            if medida_destino in opciones:
                intentos_valor = 0
                while intentos_valor < 3:
                    valor_convertir = input('Ingrese el valor a convertir (por favor, solo ingrese números): ')
                    valor_copia = valor_convertir #Guardamis una copia solo para mostrar al final el reusltado, esto es en aso de que sea un entero y al convertilro a float se le agregaria .00 al final, pro no deseamos mostrarlo asi en el resultado final
                    try:
                        valor_convertir = float(valor_convertir)
                        if medida_origen == medida_destino:
                            print(f'{valor_copia}°{medida_origen} son aproximadamente {valor_convertir}°{medida_destino}')
                            intentos_medida = 4
                            break 
                        else:
                            resultado_obtenido = llamando_operacion(medida_origen,valor_convertir,medida_destino)
                            print(f'{valor_copia}°{medida_origen} son aproximadamente {resultado_obtenido}')
                            intentos_medida = 4
                            break 
                    except Exception as e:
                        print("Por favor, ingrese un valor numérico válido")
                        intentos_valor+=1

                    if intentos_valor == 3:
                        intentos_medida = 3
                        break 

            else:
                print("La medida ingresada no esta dentro de las opciones\n")
                intentos_medida+=1
    else:
        print("La medida ingresada no esta dentro de las opciones\n")
        intentos_medida+=1

    if intentos_medida == 3:
        print("Ha exedido el limite de intentos")
        break

print("Ha salido del programa con éxito")


# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:




# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:
def factorial_calculo(numero):
    # Verifica si el número no es entero y devuelve un mensaje de error
    if type(numero) != int:
        return 'El número debe ser un entero'
    
    # Verifica si el número es negativo y devuelve un mensaje de error
    if numero < 0:
        return 'El número debe ser positivo'
    
    # Caso base: si el número es 0 o 1, el factorial es 1
    if numero <= 1:
        return 1
    
    # Recursión: calcula el factorial del número multiplicándolo por el factorial del número anterior
    # print('numero',numero)
    numero = numero * factorial_calculo(numero - 1)
    
    return numero

print(factorial_calculo(5))
print(factorial_calculo(-5))




# %%
