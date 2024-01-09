import json
campers=[]
rutas_entrenamiento=[]
entrenadores=[]
matriculas=[]
def cargar_datos():
    global campers, rutas_entrenamiento, entrenadores, matriculas
    try:
        with open("campers.json", "r") as file:
            campers = json.load(file)
    except FileNotFoundError:
        campers = []

    try:
        with open("rutas_entrenamiento.json", "r") as file:
            rutas_entrenamiento = json.load(file)
    except FileNotFoundError:
        rutas_entrenamiento = []

    try:
        with open("entrenadores.json", "r") as file:
            entrenadores = json.load(file)
    except FileNotFoundError:
        entrenadores = []
    
    try:
        with open('matriculas.json', 'r') as file:
            matriculas = json.load(file)
            if not isinstance(matriculas, list):
                matriculas = []  # Si matriculas no es una lista, inicialízala como una lista
    except FileNotFoundError:
        matriculas = []  # Ahora matriculas es una lista

    return campers, rutas_entrenamiento, entrenadores,matriculas

def guardar_datos():
    with open("campers.json", "w") as file:
        json.dump(campers, file, indent=2)

    with open("rutas_entrenamiento.json", "w") as file:
        json.dump(rutas_entrenamiento, file, indent=2)

    with open("entrenadores.json", "w") as file:
        json.dump(entrenadores, file, indent=2)
    
    with open('matriculas.json', 'w') as file:
        json.dump(matriculas, file, indent=2)
    with open('modulo.json', 'w') as file:
        matriculas = []
campers, rutas_entrenamiento, entrenadores, matriculas = cargar_datos()

def registrar_camper():
    identificacion = int(input("Ingrese el número de identificación: "))
    nombre = input("Ingrese el nombre del camper: ")
    apellidos = input("Ingrese los apellidos del camper: ")
    direccion = input("Ingrese la dirección del camper: ")
    acudiente = input("Ingrese el nombre del acudiente: ")
    telefono_celular = input("Ingrese el número de teléfono celular: ")
    telefono_fijo = input("Ingrese el número de teléfono fijo: ")
    estado = "inscrito"

    camper = {
        "identificacion": identificacion,
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefono_celular": telefono_celular,
        "telefono_fijo": telefono_fijo,
        "estado": estado,
        "ruta_entrenamiento": None,
        "nota_teoria": None,
        "nota_practica": None
    }
    campers.append(camper)
    guardar_datos()

def registrar_entrenador():
    nombre = input("Ingrese el nombre del entrenador: ")
    especialidad = input("Ingrese la especialidad del entrenador: ")
    horario = input("Ingrese el horario del entrenador: ")

    entrenador = {
        "nombre": nombre,
        "especialidad": especialidad,
        "horario": horario
    }
    entrenadores.append(entrenador)
    guardar_datos()
    print(f"Entrenador '{nombre}' registrado con éxito.")

def listar_campers():
    print("Lista de Campers:")
    for camper in campers:
        print(f"Identificación: {camper['identificacion']}")
        print(f"Nombre: {camper['nombre']} {camper['apellidos']}")
        print(f"Dirección: {camper['direccion']}")
        print(f"Acudiente: {camper['acudiente']}")
        print(f"Teléfono Celular: {camper['telefono_celular']}")
        print(f"Teléfono Fijo: {camper['telefono_fijo']}")
        print(f"Estado: {camper['estado']}")
        print(f"Ruta de Entrenamiento: {camper['ruta_entrenamiento']}")
        print(f"Nota Teoría: {camper['nota_teoria']}")
        print(f"Nota Práctica: {camper['nota_practica']}")
        print("-" * 20)

def listarCamperAprobadoInic():
    aprobados = [camper for camper in campers if camper["estado"] == "aprobado"]

    if aprobados:
        print("Campers aprobados en la prueba inicial:")
        for camper in aprobados:
            print(camper)
    else:
        print("No hay campers en este estado.")

def listarProfes():
    for profes in entrenadores:
        print(entrenadores)


def registrar_prueba(identificacion_camper):
    for camper in campers:
        if camper["identificacion"] == identificacion_camper and camper["estado"] == "inscrito":
            nota_teoria = float(input("Ingrese la nota teórica: "))
            nota_practica = float(input("Ingrese la nota práctica: "))
            promedio = (nota_teoria + nota_practica) / 2

            if promedio >= 60:
                camper["estado"] = "aprobado"
                print("Camper aprobado en las pruebas.")
            else:
                camper["estado"] = "en riesgo"
                print("Camper en riesgo. Se recomienda revisar su desempeño.")

            camper["nota_teoria"] = nota_teoria
            camper["nota_practica"] = nota_practica
            guardar_datos()
            return
    print("No se pudo registrar la prueba. Verifique la identificación del camper o su estado.")

def registrar_ruta_entrenamiento():
    nombre_ruta = input("Ingrese el nombre de la ruta de entrenamiento: ")
    areas_entrenamiento = input("Ingrese las áreas de entrenamiento (separadas por comas): ").split(',')
    capacidad_maxima = int(input("Ingrese la capacidad máxima de campers: "))
    sgdb_principal = input("Ingrese el SGDB principal: ")
    sgdb_alternativo = input("Ingrese el SGDB alternativo: ")

    ruta = {
        "nombre": nombre_ruta,
        "areas_entrenamiento": areas_entrenamiento,
        "capacidad_maxima": capacidad_maxima,
        "sgdb_principal": sgdb_principal,
        "sgdb_alternativo": sgdb_alternativo,
        "campers_asignados": [],
        "entrenador_asignado": None
    }
    rutas_entrenamiento.append(ruta)
    guardar_datos()
    print(f"Ruta de entrenamiento '{nombre_ruta}' registrada con éxito.")

campers, rutas_entrenamiento, entrenadores, matriculas = cargar_datos()

def asignar_matricula():
    global campers, matriculas
    id_camper = int(input("Ingrese el número de identificación del camper: "))

    for camper in campers:
        if camper["identificacion"] == id_camper:
            estado_camper = camper["estado"].strip().lower()

            if estado_camper == "aprobado":
                ruta = input("Ingrese la ruta de entrenamiento: ")
                fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                fecha_fin = input("Ingrese la fecha de finalización (YYYY-MM-DD): ")
                salon = input("Ingrese el salón de entrenamiento: ")

                nueva_matricula = {
                    "camper_id": id_camper,
                    "ruta": ruta,
                    "fecha_inicio": fecha_inicio,
                    "fecha_fin": fecha_fin,
                    "salon": salon
                }

                matriculas.append(nueva_matricula)

                # Actualizar estado del camper a "Matriculado"
                camper["estado"] = "Matriculado"
                for camper in campers:
                    if "ruta_entrenamiento" in camper:
                        modulo_info = {
                        "id_camper": camper["identificacion"],
                        "ruta_asignada": camper["ruta_entrenamiento"],
                        "profesor_asignado": None  # Puedes asignar al profesor si es información que tienes
                        }
                        modulo_data.append(modulo_info)

        

                print("Matrícula asignada con éxito.")
                guardar_datos()
                return
            else:
                print("El camper no está en estado aprobado para matricular.")
                return
            

    print("No se encontró ningún camper con el número de identificación proporcionado.")

# 
def buscar_profesor_disponible(areas_entrenamiento):
    # Aquí deberías implementar la lógica para buscar un profesor disponible
    # en función de las áreas de entrenamiento especificadas.
    # Retorna el profesor disponible o None si no hay profesores disponibles.

    # Ejemplo básico: simplemente devuelve el primer entrenador disponible.
    for entrenador in entrenadores:
        if entrenador["especialidad"] in areas_entrenamiento:
            return entrenador

    return None  # Retorna None si no se encuentra un profesor disponible para las áreas de entrenamiento.


import json

def guardar_modulo_json(campers, rutas_entrenamiento):
    modulo_data = []
    for camper in campers:
        if "ruta_entrenamiento" in camper:
            for ruta in rutas_entrenamiento:
                if ruta["nombre"] == camper["ruta_entrenamiento"]:
                    modulo_info = {
                        "id_camper": camper["identificacion"],
                        "ruta_asignada": camper["ruta_entrenamiento"],
                        "profesor_asignado": ruta.get("entrenador_asignado", "")
                    }
                    modulo_data.append(modulo_info)

    try:
        with open('modulo.json', 'w') as file:
            json.dump(modulo_data, file, indent=2)
        print("Datos guardados en 'modulo.json' correctamente.")
    except Exception as e:
        print(f"Error al guardar en 'modulo.json': {e}")

def asignar_ruta_entrenamiento(identificacion_camper, nombre_ruta):
    global campers, rutas_entrenamiento, matriculas, entrenadores

    for camper in campers:
        if camper["identificacion"] == identificacion_camper and camper["estado"] == "aprobado":
            for ruta in rutas_entrenamiento:
                if ruta["nombre"] == nombre_ruta and len(ruta["campers_asignados"]) < ruta["capacidad_maxima"]:
                    # Asignar ruta al camper
                    camper["ruta_entrenamiento"] = ruta["nombre"]
                    ruta["campers_asignados"].append(camper["identificacion"])

                    # Información para matricula.json
                    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                    fecha_fin = input("Ingrese la fecha de finalización (YYYY-MM-DD): ")
                    salon = input("Ingrese el salón de entrenamiento: ")

                    nueva_matricula = {
                        "camper_id": identificacion_camper,
                        "ruta": nombre_ruta,
                        "fecha_inicio": fecha_inicio,
                        "fecha_fin": fecha_fin,
                        "salon": salon
                    }

                    matriculas.append(nueva_matricula)

                    # Permitir al usuario ingresar el nombre del entrenador sin validación
                    nombre_entrenador = input("Ingrese el nombre del entrenador: ")
                    ruta["entrenador_asignado"] = nombre_entrenador
                    print(f"Entrenador {nombre_entrenador} asignado a la ruta '{nombre_ruta}'.")

                    # Actualizar estado del estudiante a "Matriculado"
                    camper["estado"] = "Matriculado"

                    # Guardar información en modulo.json llamando a la función separada
                    guardar_modulo_json(campers, rutas_entrenamiento)

                    guardar_datos()
                    print(f"Camper asignado a la ruta '{nombre_ruta}' con éxito y matriculado.")
                    return

    print(f"No se pudo asignar la ruta '{nombre_ruta}'. La ruta está llena o el camper no está aprobado.")

def registrar_prueba_modulo(identificacion_camper):
    for camper in campers:
        if camper["identificacion"] == identificacion_camper and camper["estado"] == "Matriculado":
            nota_teoria_modulo = float(input("Ingrese la nota teórica del módulo: "))
            nota_practica_modulo = float(input("Ingrese la nota práctica del módulo: "))
            nota_quices_trabajos = float(input("Ingrese la nota de quices y trabajos del módulo: "))
            nota_final = (nota_teoria_modulo * 0.3) + (nota_practica_modulo * 0.6) + (nota_quices_trabajos * 0.1)

            # Actualizar la estructura del camper con las notas
            camper["nota_teoria"] = nota_teoria_modulo
            camper["nota_practica"] = nota_practica_modulo
            camper["nota_quices_trabajos"] = nota_quices_trabajos
            camper["nota_final"] = nota_final

            # Actualizar el estado del camper
            if nota_final >= 60:
                camper["estado"] = "aprobado"
                print("Camper aprobado en las pruebas.")
            else:
                camper["estado"] = "en riesgo"
                print("Camper en riesgo. Se recomienda revisar su desempeño.")

            # Actualizar el estado en matriculas.json
            for matricula in matriculas:
                if matricula["camper_id"] == identificacion_camper and matricula["ruta"] == camper["ruta_entrenamiento"]:
                    matricula["estado"] = camper["estado"]
                    break

            guardar_datos()
            return

    print("No se pudo registrar la prueba. Verifique la identificación del camper o su estado.")

def listar_campers_en_riesgo():
    abuscar = "en riesgo"
    for matricula in matriculas:
        if "estado" in matricula and matricula["estado"] == abuscar:
            print(matricula)


def listar_campers_por_estado():
    en_riesgo = 0
    aprobados = 0
    for matricula in matriculas:
        if "estado" in matricula:
            if matricula["estado"] == "en riesgo":
                en_riesgo += 1
            elif matricula["estado"] == "aprobado":
                aprobados += 1
    
    print(f"Campers en riesgo: {en_riesgo}")
    print(f"Campers aprobados: {aprobados}")

# Ejemplo de uso



# Llama a esta función después de haber asignado rutas y entrenadores


# Luego puedes llamar a esta función en tu código principal


# def asignar_ruta_entrenamiento(identificacion_camper, nombre_ruta):
#     for camper in campers:
#         if camper["identificacion"] == identificacion_camper and camper["estado"] == "aprobado":
#             for ruta in rutas_entrenamiento:
#                 if ruta["nombre"] == nombre_ruta and len(ruta["campers_asignados"]) < ruta["capacidad_maxima"]:
#                     camper["ruta_entrenamiento"] = ruta["nombre"]
#                     ruta["campers_asignados"].append(camper["identificacion"])
#                     guardar_datos()
#                     print(f"Camper asignado a la ruta '{nombre_ruta}' con éxito.")
#                     return
#             print(f"No se pudo asignar la ruta '{nombre_ruta}'. La ruta está llena.")
#             return
#     print("No se pudo asignar la ruta. Verifique la identificación del camper o su estado.")

# def evaluar_estado_y_asignar_ruta(identificacion_camper):
#     for camper in campers:
#         if camper["identificacion"] == identificacion_camper and camper["estado"] == "aprobado":
#             asignar_ruta = input(f"El camper {camper['nombre']} {camper['apellidos']} está aprobado. ¿Desea asignarle una ruta de entrenamiento? (Sí/No): ").lower()
#             if asignar_ruta == "si":
#                 nombre_ruta = input("Ingrese el nombre de la ruta de entrenamiento: ")
#                 asignar_ruta_entrenamiento(identificacion_camper, nombre_ruta)
#             return
#     print("Camper no encontrado o no cumple con las condiciones para asignar una ruta.")

