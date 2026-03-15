import random

# carreras
carreras = ["Ingeniería en Sistemas", "Licenciatura en Nutrición", "Abogacía"]

# cantidad de listas
cant_listas = int(input("Ingrese cantidad de listas: "))

# nombres de listas
listas = []
for i in range(cant_listas):
    nombre = input(f"Nombre de la lista {i+1}: ")
    listas.append(nombre)

# matriz de votos
votos = []
for i in range(len(carreras)):
    votos.append([0] * cant_listas)

MAX_VOTOS = 300


# generar votos aleatorios
def generar_votos():
    for i in range(len(carreras)):

        print("\nCarrera:", carreras[i])

        votos_restantes = MAX_VOTOS

        for j in range(cant_listas):

            if j == cant_listas - 1:
                voto = votos_restantes
            else:
                voto = random.randint(0, votos_restantes)

            votos[i][j] = voto
            votos_restantes -= voto

            print(listas[j], "->", voto, "votos")


# calcular lista ganadora
def lista_ganadora():
    totales = [0] * cant_listas

    for i in range(len(carreras)):
        for j in range(cant_listas):
            totales[j] += votos[i][j]

    ganador = totales.index(max(totales))

    print("\nLista ganadora:", listas[ganador])
    print("Votos:", totales[ganador])


# calcular porcentajes
def porcentajes():
    totales = [0] * cant_listas
    total_general = 0

    for i in range(len(carreras)):
        for j in range(cant_listas):
            totales[j] += votos[i][j]
            total_general += votos[i][j]

    print("\nPorcentaje de votos:")
    for j in range(cant_listas):
        porcentaje = (totales[j] / total_general) * 100
        print(listas[j], ":", round(porcentaje, 2), "%")


# buscar votos por lista y carrera
def buscar_votos():
    print("\nCarreras:")
    for i in range(len(carreras)):
        print(i, "-", carreras[i])

    c = int(input("Seleccione carrera: "))

    print("\nListas:")
    for j in range(cant_listas):
        print(j, "-", listas[j])

    l = int(input("Seleccione lista: "))

    print("Votos obtenidos:", votos[c][l])


# programa principal
def main():
    generar_votos()
    lista_ganadora()
    porcentajes()
    buscar_votos()


main()