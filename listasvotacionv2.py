# mejoras implementadas: el usuario decide cuántas listas hay
# no se pueden cargar más votos que los estudiantes habilitados (máximo 300 por carrera)
# validaciones para que no se ingresen números negativos ni se exceda el límite

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


# cargar votos
def cargar_votos():
    for i in range(len(carreras)):
        print("\nCarrera:", carreras[i])

        suma_carrera = 0

        for j in range(cant_listas):

            while True:
                voto = int(input(f"Votos para {listas[j]}: "))

                if voto < 0:
                    print("Error: los votos no pueden ser negativos")

                elif suma_carrera + voto > MAX_VOTOS:
                    print("Error: se supera el máximo de 300 votos en esta carrera")

                else:
                    votos[i][j] = voto
                    suma_carrera += voto
                    break


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
    cargar_votos()
    lista_ganadora()
    porcentajes()
    buscar_votos()


main()