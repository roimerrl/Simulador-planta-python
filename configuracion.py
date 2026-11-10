""" Este modulo permite establecer la presentacion inicial del simulador y definir
 las condiciones de arranque de la planta segun el escenario que elija
 el usuario. Aqui no se realizan calculos de producción, solo se preparan los
 valores base que main.py va a necesitar despues en las 5 jornadas. 
 """

from validaciones import leer_entero_en_rango, leer_texto  # importacion de lecturas con try-except

def bienvenida():
    # Se muestra el banner del sistema y pide los dos primeros valores
    # se aplica la funcion predefinida  leer_texto para que no acepte nombres vacios
    print("==================================================")
    print("  SIMULADOR DE GESTIÓN DE PLANTA DE PRODUCCIÓN    ")
    print("==================================================")
    nombre_planta = leer_texto("Ingrese el nombre de la planta: ")
    supervisor = leer_texto("Ingrese el nombre del supervisor: ")
    # Se devuelven dos valores porque main.py los necesita por separado
    return nombre_planta, supervisor

def seleccionar_escenario():
    """ Aqui el usuario elige el nivel de dificultad de la simulacion
     1 = condiciones normales, 2 = más demanda, 3 = recursos limitados.
     se aplica la funcion predefinida leer_entero_en_rango se encarga
     de que solo entre 1, 2 o 3.
     """

    print("\n--- SELECCION DE ESCENARIO ---")
    print("1. Producción Estable (Condiciones normales)")
    print("2. Alta Demanda (Mayor presion operativa)")
    print("3. Producción Critica (Recursos reducidos)")
    opcion = leer_entero_en_rango("Seleccione un escenario (1-3): ", 1, 3)
    return opcion

def inicializar_materia_prima(escenario):
    """ Cantidad inicial de materia prima en kg según el escenario
     el escenario 3 tiene menos materiaprima que los otros dos, es a proposito
     para simular una planta con restricciones
     850 kg es suficiente para las 5 jornadas en el escenario critico 
     """

    if escenario == 1:
        return 1200.0
    elif escenario == 2:
        return 1400.0
    else:
        return 850.0

def inicializar_horas(escenario):
    """Total de horas disponibles para toda la simulacion (se reparten
     entre las 5 jornadas dentro de main.py)
     Escenario 2 tiene más horas porque hay mas demanda, y el 3 tiene
     menos horas porque es el escenario critico
     """

    if escenario == 1:
        return 40.0
    elif escenario == 2:
        return 48.0
    else:
        return 30.0

def inicializar_meta_jornada(escenario):
    """ Meta de unidades que se esperan producir por jornada
     Es lo que se usa para calcular el cumplimiento y la eficiencia
     la meta es diaria, no total, main.py la debe de ir sumando jornada
     por jornada para obtener el plan total"""

    if escenario == 1:
        return 200
    elif escenario == 2:
        return 280
    else:
        return 160

def mostrar_parametros_iniciales(nombre_planta, supervisor, escenario, mp, horas, meta_dia):
    """Muestra los valores con los que arranca la simulacion lo cual es meramente informativo"""
    print("\n===============================================")
    print("             PARAMETROS INICIALES                 ")
    print("==================================================")
    print(f"Planta: {nombre_planta}")
    print(f"Supervisor: {supervisor}")
    if escenario == 1:
        nombre_esc = "Producción Estable"
    elif escenario == 2:
        nombre_esc = "Alta Demanda"
    else:
        nombre_esc = "Producción Critica"
    print(f"Escenario: {escenario} - {nombre_esc}")
    print(f"Materia prima disponible: {mp:.1f} kg")
    print(f"Horas disponibles totales: {horas:.1f} h")
    print(f"Meta por jornada: {meta_dia} unidades")
    print(f"Meta total (5 jornadas): {meta_dia * 5} unidades")
    print("==============================================")
