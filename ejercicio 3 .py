def max_vocales(s, k):
    vocales = "aeiouAEIOU"
    maximo = 0

    for i in range(len(s) - k + 1):
        subcadena = s[i:i+k]
        contador = 0

        for letra in subcadena:
            if letra in vocales:
                contador += 1

        if contador > maximo:
            maximo = contador

    return maximo


# Pedir datos al usuario
s = input("Ingrese una palabra o frase: ")
k = int(input("Ingrese el valor de k: "))

resultado = max_vocales(s, k)

print("El máximo número de vocales en una subcadena de longitud", k, "es:", resultado)