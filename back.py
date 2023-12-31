import random
import csv

# Estructuras de datos
clases_disponibles = {} 

salones = {f'X{i}': {} for i in range(1, 23)}

profesores = {}

# Función para cargar clases desde un archivo CSV
def cargar_clases_desde_csv():
    with open("Libro1.csv", newline='', encoding='utf-8') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for row in reader:
            if len(row) >= 2:
                clases_disponibles[row[0]] = {'Duracion': int(row[1])}

# Cargar clases al inicio del programa
cargar_clases_desde_csv()

# Actualización de la función generar_horarios() y funciones relacionadas

def generar_horarios():
    for salon in salones:
        for dia in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']:
            horario = generar_horario(dia)
            salones[salon][dia] = horario

def generar_horario(dia):
    horario = []

    # Obtener todas las clases disponibles
    clases_disponibles_hoy = list(clases_disponibles.keys())

    # Mezclar la lista para una selección aleatoria
    random.shuffle(clases_disponibles_hoy)

    for clase in clases_disponibles_hoy:
        duracion = clases_disponibles[clase]['Duracion']

        # Verificar si hay espacio disponible en el horario para esta clase
        if hay_espacio_para_clase(horario, duracion):
            # Añadir la clase con su horario correspondiente
            horario_clase = {'Clase': clase, 'Horario': obtener_horario_disponible(horario, duracion, dia), 'Dia': dia}
            horario.append(horario_clase)

    return horario

# Actualización de la función obtener_horario_disponible()
# y función relacionada

def obtener_horario_disponible(horario, duracion, dia):
    horas_disponibles = list(range(9, 16, 2))  # Cambio en el rango horario
    for clase_existente in horario:
        if clase_existente['Dia'] == dia:
            for hora_inicio, hora_fin in clase_existente['Horario']:
                horas_disponibles = [h for h in horas_disponibles if h not in range(hora_inicio, hora_fin)]
    
    horario_clase = []
    while duracion > 0 and horas_disponibles:
        hora = random.choice(horas_disponibles)
        horario_clase.append((hora, hora + 2))  # Asignar bloques de 2 horas
        horas_disponibles.remove(hora)
        duracion -= 2
    
    return horario_clase

# Actualización de la función hay_espacio_para_clase()
# y función relacionada

def hay_espacio_para_clase(horario, duracion):
    # Verificar si hay suficiente espacio para la nueva clase
    horas_disponibles = list(range(9, 18, 2))  # Cambio en el rango horario
    for clase_existente in horario:
        for hora_inicio, hora_fin in clase_existente['Horario']:
            horas_disponibles = [h for h in horas_disponibles if h not in range(hora_inicio, hora_fin)]
    
    return len(horas_disponibles) >= duracion

def siguiente_dia(dia):
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    indice_dia = dias.index(dia)
    siguiente_indice = (indice_dia + 1) % len(dias)
    return dias[siguiente_indice]

# Función para añadir profesor a un salón y materia
def añadir_profesor():
    salon = input("Ingrese el nombre del salón: ")
    materia = input("Ingrese el nombre de la materia: ")
    profesor = input("Ingrese el nombre del profesor: ")

    if salon in salones and materia in clases_disponibles:
        for dia, horario in salones[salon].items():
            for clase in horario:
                if clase['Clase'] == materia:
                    clase['Profesor'] = profesor
                    print(f"Profesor {profesor} asignado a {materia} en {salon}.")
                    return  # Salir de la función después de asignar el profesor

        # Si llega aquí, la materia no fue encontrada en el horario del salón
        print(f"Error: La materia {materia} no encontrada en el horario del salón {salon}.")
    else:
        print("Error: Salón o materia no encontrados.")


# Función para mostrar horarios
def mostrar_horarios():
    for salon, horarios in salones.items():
        print(f"\nSalón: {salon}")
        for dia, horario in horarios.items():
            print(f"\n{dia}:")
            for clase in horario:
                profesor = clase.get('Profesor', 'Sin asignar')
                print(f"  {clase['Clase']} - {clase['Horario']} - Profesor: {profesor}")

# Función para mostrar el horario de un salón específico
def mostrar_horario_salon():
    salon = input("Ingrese el nombre del salón: ")
    if salon in salones:
        print(f"\nHorario del Salón {salon}:")
        for dia, horario in salones[salon].items():
            print(f"\n{dia}:")
            for clase in horario:
                profesor = clase.get('Profesor', 'Sin asignar')
                print(f"  {clase['Clase']} - {clase['Horario']} - Profesor: {profesor}")
    else:
        print("Error: Salón no encontrado.")

# Funcion para editar materias
# Función para editar materias
def editar_materia():
    print("\n--- Editar Materia ---")
    salon = input("Ingrese el nombre del salón: ").upper()
    dia = input("Ingrese el día (Lunes, Martes, Miércoles, Jueves o Viernes): ")

    if salon not in salones or dia not in salones[salon]:
        print("Error: Salón o día no encontrados en el horario.")
        return

    # Mostrar las materias actuales para seleccionar cuál editar
    print("\nMaterias en este horario:")
    for i, clase in enumerate(salones[salon][dia]):
        print(f"{i + 1}. {clase['Clase']} - {clase['Horario']}")

    # Pedir al usuario que elija una materia
    try:
        opcion_materia = int(input("\nSeleccione el número de la materia que desea editar: ")) - 1
        materia_editar = salones[salon][dia][opcion_materia]['Clase']
    except (ValueError, IndexError):
        print("Error: Selección no válida.")
        return

    print("\n--- Opciones de Edición ---")
    print("1. Editar Horario")
    print("2. Editar Nombre de la Materia")
    print("3. Eliminar Materia")
    print("4. Añadir Materia Manualmente")
    print("5. Cancelar")

    opcion_edicion = input("\nSeleccione una opción: ")

    if opcion_edicion == '1':
        # Editar horario de la materia seleccionada
        nuevo_horario = obtener_horario_disponible(salones[salon][dia], clases_disponibles[materia_editar]['Duracion'], dia)
        salones[salon][dia][opcion_materia]['Horario'] = nuevo_horario
        print(f"Horario de {materia_editar} actualizado a {nuevo_horario} en {dia}.")
    elif opcion_edicion == '2':
        # Editar nombre de la materia
        nuevo_nombre = input("Ingrese el nuevo nombre de la materia: ")
        if nuevo_nombre in clases_disponibles:
            salones[salon][dia][opcion_materia]['Clase'] = nuevo_nombre
            print(f"Nombre de la materia actualizado a {nuevo_nombre} en {dia}.")
        else:
            print(f"Error: La materia {nuevo_nombre} no existe en el registro.")
    elif opcion_edicion == '3':
        # Eliminar materia
        salones[salon][dia].pop(opcion_materia)
        print(f"{materia_editar} eliminada del horario en {dia}.")
    elif opcion_edicion == '4':
        # Añadir materia manualmente
        nueva_materia = input("Ingrese el nombre de la nueva materia: ")
        if nueva_materia not in clases_disponibles:
            print("Error: La materia no existe en el registro.")
            return
        nuevo_horario = obtener_horario_disponible(salones[salon][dia], clases_disponibles[nueva_materia]['Duracion'], dia)
        salones[salon][dia].append({'Clase': nueva_materia, 'Horario': nuevo_horario})
        print(f"{nueva_materia} añadida al horario en {dia}.")
    elif opcion_edicion == '5':
        # Cancelar
        print("Operación cancelada.")
    else:
        print("Opción no válida.")

# Menú principal
while True:
    print("\n--- Menú ---")
    print("1. Generar Horarios")
    print("2. Añadir Profesor")
    print("3. Mostrar Horarios")
    print("4. Mostrar Horario de un Salón")
    print("5. Salir")
    print("6. Editar materias")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        generar_horarios()
        print("Horarios generados exitosamente.")
    elif opcion == '2':
        añadir_profesor()
    elif opcion == '3':
        mostrar_horarios()
    elif opcion == '4':
        mostrar_horario_salon()
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    elif opcion == '6':
        editar_materia()
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")

