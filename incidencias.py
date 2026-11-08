from validaciones import leer_entero_en_rango  # importamos la funcion de validacion de numeros enteros en rango


"""Se define el modulo de incidencias, que contiene la funcion aplicar_incidencia, 
que se encarga de mostrar las incidencias y pedir al usuario que elija una opcion para resolverla.
asi cada opción ajusta las variables de la simulación (costos, tiempo, materia prima y estado de la máquina)."""


def aplicar_incidencia(jornada):
    print("\n--------------------------------------------------")
    print("                 INCIDENCIA DETECTADA             ")
    print("--------------------------------------------------")
    
    costo_extra = 0.0
    horas_perdidas_extra = 0.0
    mp_extra = 0.0
    nuevo_estado_maquina = 1
    
    if jornada == 1:
        print("Incidencia: Falla mecanica leve en el motor principal.")
        print("1. Reparacion inmediata (Costo $150, pierde 2 horas, maquina queda al 100%)")
        print("2. Ajuste rapido y continuar (Sin costo, pierde 0 horas, maquina queda con fallas)")
        print("3. No intervenir (Sin costo, pierde 0 horas, pero maquina averiada aumenta defectos)")
        opcion = leer_entero_en_rango("Opcion (1-3): ", 1, 3)
        if opcion == 1:
            costo_extra = 150.0
            horas_perdidas_extra = 2.0
            nuevo_estado_maquina = 1
        elif opcion == 2:
            nuevo_estado_maquina = 0
        else:
            nuevo_estado_maquina = 0

    elif jornada == 2:
        print("Incidencia: Lote de materia prima con retraso logistico.")
        print("1. Comprar lote local de emergencia (Costo $200, suma 100 kg MP)")
        print("2. Esperar al proveedor (Pierde 3 horas, sin costo)")
        print("3. Trabajar solo con inventario existente (Sin costo, riesgo de parar)")
        opcion = leer_entero_en_rango("Opcion (1-3): ", 1, 3)
        if opcion == 1:
            costo_extra = 200.0
            mp_extra = 100.0
        elif opcion == 2:
            horas_perdidas_extra = 3.0

            """Ya no aguanto mas el sueño T_T aguantenme un rato"""