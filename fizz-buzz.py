# Programa para imprimir números del 1 al 100 con condiciones específicas

for i in range(1, 101):  # Iteramos desde 1 hasta 100
    if i % 3 == 0 and i % 5 == 0:  # Comprobamos si el número es múltiplo de 3 y 5
        print("fizzbuzz")
    elif i % 3 == 0:  # Comprobamos si el número es múltiplo de 3
        print("fizz")
    elif i % 5 == 0:  # Comprobamos si el número es múltiplo de 5
        print("buzz")
    else:  # Si no cumple ninguna de las condiciones anteriores, imprimimos el número
        print(i)

# Nota: Los llamados a funciones están comentados para cumplir con las instrucciones de desarrollo.
