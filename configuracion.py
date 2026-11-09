""" Este modulo permite establecer la presentacion inicial del simulador y definir
 las condiciones de arranque de la planta segun el escenario que elija
 el usuario. Aqui no  se realizan calculos de producciòn, solo se preparan los
 valores base que main.py va a necesitar despues en las 5 jornadas. """

from validaciones import leer_entero_en_rango, leer_texto  # importacion de lecturas con try-except

def bienvenida():
    # Se muestra el banner del sistema y pide los dos primeros valores.
    # se aplica la funcion predefinida  leer_texto para que no acepte nombres vacios.
    print("==================================================")
    print("  SIMULADOR DE GESTIÒN DE PLANTA DE PRODUCCIÒN    ")
    print("==================================================")
    nombre_planta = leer_texto("Ingrese el nombre de la planta: ")
    supervisor = leer_texto("Ingrese el nombre del supervisor: ")
    # Se devuelven dos valores porque main.py los necesita por separado
    return nombre_planta, supervisor

def seleccionar_escenario():
    """ Aquì el usuario elige el nivel de dificultad de la simulacion.
     1 = condiciones normales, 2 = màs demanda, 3 = recursos limitados.
     se aplica la funcion predefinida leer_entero_en_rango se encarga
     de que solo entre 1, 2 o 3."""
    
    print("\n--- SELECCION DE ESCENARIO ---")
    print("1. Producciòn Estable (Condiciones normales)")
    print("2. Alta Demanda (Mayor presion operativa)")
    print("3. Producciòn Critica (Recursos reducidos)")
    opcion = leer_entero_en_rango("Seleccione un escenario (1-3): ", 1, 3)
    return opcion



def inicializar_materia_prima(escenario):
    """" Cantidad inicial de materia prima en kg segùn el escenario
     el escenario 3 tiene menos MP que los otros dos, es a proposito
     para simular una planta con restricciones
     850 kg es suficiente para las 5 jornadas en el escenario critico """
    
    if escenario == 1:
        return 1200.0
    elif escenario == 2:
        return 1400.0
    else:
        return 850.0

    

def inicializar_horas(escenario):
    """Total de horas disponibles para toda la simulacion (se reparten
     entre las 5 jornadas dentro de main.py)
     Escenario 2 tiene màs horas porque hay mas demanda, y el 3 tiene
     menos horas porque es el escenario critico"""
    
    if escenario == 1:
        return 40.0
    elif escenario == 2:
        return 48.0
    else:
        return 30.0



def inicializar_meta_jornada(escenario):
    """ Meta de unidades que se esperan producir por jornada
     Es lo que se usa para calcular el cumplimiento y la eficiencia
     la meta es diaria, no total. main.py la debe de ir sumando jornada
     por jornada para obtener el plan total"""
    
    if escenario == 1:
        return 200
    elif escenario == 2:
        return 280
    else:
        return 160