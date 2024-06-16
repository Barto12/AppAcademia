class Carrera:
    def __init__(self, cve_carrera, desc_carrera):
        self.cve_carrera = cve_carrera
        self.desc_carrera = desc_carrera


class Alumno:
    def __init__(self, no_control, nombre, genero, carrera):
        self.no_control = no_control
        self.nombre = nombre
        self.genero = genero
        self.carrera = carrera


def mostrar_menu():
    print("1. Agregar carreras")
    print("2. Agregar alumnos")
    print("3. Listar alumnos")
    print("4. Salir")


def agregar_carrera(carreras):
    try:
        cve_carrera = input("Clave de la carrera: ").strip()
        desc_carrera = input("Descripción de la carrera: ").strip()
        if not cve_carrera or not desc_carrera:
            raise ValueError("Todos los campos son obligatorios.")
        carreras.append(Carrera(cve_carrera, desc_carrera))
        print("Carrera agregada exitosamente.")
    except ValueError as e:
        print(e)


def agregar_alumno(alumnos, carreras):
    try:
        no_control = input("Número de control: ").strip()
        nombre = input("Nombre del alumno: ").strip()
        genero = input("Género del alumno: ").strip()
        if not no_control or not nombre or not genero:
            raise ValueError("Todos los campos son obligatorios.")

        print("Carreras disponibles:")
        for idx, carrera in enumerate(carreras):
            print(f"{idx + 1}. {carrera.desc_carrera}")
        carrera_idx = int(input("Selecciona la carrera (número): ")) - 1
        if carrera_idx < 0 or carrera_idx >= len(carreras):
            raise ValueError("Selección de carrera inválida.")

        alumnos.append(Alumno(no_control, nombre, genero, carreras[carrera_idx]))
        print("Alumno agregado exitosamente.")
    except ValueError as e:
        print(e)


def listar_alumnos(alumnos):
    if alumnos:
        print("No_control | Nombre | Carrera")
        for alumno in alumnos:
            print(f"{alumno.no_control} | {alumno.nombre} | {alumno.carrera.desc_carrera}")
    else:
        print("No hay alumnos registrados.")


def main():
    carreras = []
    alumnos = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            agregar_carrera(carreras)
        elif opcion == '2':
            if carreras:
                agregar_alumno(alumnos, carreras)
            else:
                print("Primero debes agregar carreras.")
        elif opcion == '3':
            listar_alumnos(alumnos)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
