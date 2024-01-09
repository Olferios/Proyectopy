from campers import *
from util import*
from menus import*
#bootstrap


# funtions
def campers():      
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
       registrar_camper()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listar_campers()
       input("Clic cualquier teclas [continuar]: ")
def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
    if op==1:
       registrar_entrenador()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       registrar_ruta_entrenamiento()
       input("Clic cualquier teclas [continuar]: ")
    
def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
    if op==1:
       identificacion_prueba = int(input("Ingrese la identificación del camper para la prueba: "))
       registrar_prueba(identificacion_prueba)
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listarCamperAprobadoInic()
       input("Clic cualquier teclas [continuar]: ")
    if op==3:
        identificacion_camper=int(input("ingrese id camper"))
        nombre_ruta=input("ingrese nombre ruta")
        asignar_ruta_entrenamiento(identificacion_camper, nombre_ruta)
        input("clic cualquier tecla[continuar]:")
    if op==4:
        identificacion_camper = int(input("Ingrese el número de identificación del camper: "))
        registrar_prueba_modulo(identificacion_camper)
        
        

def aulas():
    limpiar_pantalla()    
    op=menu_aulas()
def reportes():
    limpiar_pantalla()    
    op=menu_reportes()
    if op==1:
        listar_campers()
        input("Clic cualquier teclas [continuar]: ")
    if op==2:
        listarCamperAprobadoInic()
        input("Clic cualquier teclas [continuar]: ")
    if op==3:
        
        listarProfes()
        input("clic cualquier tecla[continuar]:")
    
    if op==4:
        
        listar_campers_en_riesgo()
        input("clic cualquier tecla[continuar]:")
    if op==6:
        listar_campers_por_estado()


    

#start
while True: 
   limpiar_pantalla()
   op=menu_principal()
   if  op==1:
       campers()
   elif op==2:
       trainers()
   elif op==3:
       matriculas()
   elif op==4:
       aulas()
   elif op==5:
       reportes()
   elif op==6:
       print("Saliendo")
       break
       