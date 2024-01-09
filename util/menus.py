from util import validar_opcion

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Campers")
    print("2. Trainers")
    print("3. Matriculas")
    print("4. Aulas")
    print("5. Reportes")
    print("6. Salir")       
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_campers():
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. listar campers")
    print("3. Salir")
    op=validar_opcion("Opcion: ",1,3)
    return op
    
    
def menu_trainers():
    print("----------- Menú Trainers-----------")
    print("1. Crear trainer")
    print("2. Crear ruta entrenamiento")
    print("3. Modificar trainer")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_matriculas():
    print("----------- Menú Matriculas-----------")
    print("1. Ingresar evaluacion inciaal")
    print("2. Buscar Matriculas")
    print("3. Modificar Matriuclas")
    print("4. registrar evaluaciones")
    op=validar_opcion("Opcion: ",1,5)
    return op

def menu_aulas():
    print("----------- Menú Aulas-----------")
    print("1. Crear Aulas")
    print("2. Buscar Aulas")
    print("3. Modificar Aulas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_reportes():
    print("----------- Menú Reportes-----------")
    print("1. Listar campers estado inscripto")
    print("2. Listar campers aprobaron examen")
    print("3. Listar trainers trabajando en campus")
    print("4. Listar estudiantes con bajo rendimiento")
    print("5. Listar campers y entrenador a una ruta")
    print("6. mostrar campers que perdieron y aprobaron cada uno de los modulos")
    print("7. Salir")
    
    op=validar_opcion("Opcion: ",1,7)
    return op