# carreras y listas
carreras = ["Ingeniería en Sistemas", "Licenciatura en Nutrición", "Abogacía"]
listas = ["Lista 1", "Lista 2", "Lista 3"]

# matriz de votos (3 carreras x 3 listas)
votos = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


# a) cargar votos
def cargar_votos():
    for i in range(3):
        print("\nCarrera:", carreras[i])
        for j in range(3):
            votos[i][j] = int(input(f"Ingrese votos para {listas[j]}: "))


# b) lista ganadora
def lista_ganadora():
    totales = [0, 0, 0]

    for i in range(3):
        for j in range(3):
            totales[j] += votos[i][j]

    ganador = totales.index(max(totales))

    print("\nLista ganadora:", listas[ganador])
    print("Votos:", totales[ganador])


# c) porcentaje de votos
def porcentajes():
    totales = [0, 0, 0]
    total_general = 0

    for i in range(3):
        for j in range(3):
            totales[j] += votos[i][j]
            total_general += votos[i][j]

    print("\nPorcentaje de votos:")
    for j in range(3):
        porcentaje = (totales[j] / total_general) * 100
        print(listas[j], ":", round(porcentaje, 2), "%")


# d) buscar votos por carrera y lista
def buscar_votos():
    print("\nCarreras:")
    for i in range(3):
        print(i, "-", carreras[i])

    c = int(input("Seleccione carrera: "))

    print("\nListas:")
    for j in range(3):
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