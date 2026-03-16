binario = input("Ingrese un número binario de 8 bits: ")

decimal = 0
potencia = 7

for bit in binario:
    decimal += int(bit) * (2 ** potencia)
    potencia -= 1

print("El equivalente en decimal es:", decimal)