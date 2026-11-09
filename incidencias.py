from validaciones import leer_entero_en_rango  # importamos la funcion de validacion de numeros enteros en rango


"""Se define el modulo de incidencias, que contiene la funcion aplicar_incidencia, 
que se encarga de mostrar las incidencias y pedir al usuario que elija una opcion para resolverla.
asi cada opción ajusta las variables de la simulación (costos, tiempo, materia prima y estado de la máquina)."""


def aplicar_incidencia(jornada, estado_actual):
    print("\n--------------------------------------------------")
    print(f"          INCIDENCIA DE LA JORNADA {jornada}             ")
    print("--------------------------------------------------")
    
    costo_extra = 0.0
    horas_perdidas_extra = 0.0
    mp_extra = 0.0
    nuevo_estado_maquina = estado_actual  # Inicialmente el estado de la máquina no cambia
    

    # ------------ Jornada 1 -----------------
    if jornada == 1:
        print("Incidencia: Falla mecanica leve en el motor principal.")
        print("1. Reparacion inmediata (Costo $150, pierde 2 horas, maquina queda al 100%)")
        print("2. Ajuste rapido y continuar (Costo $40, maquina queda inestable)")
        print("3. No intervenir (Sin costo, la maquina se detiene a mitad del turno, pierde 1.5 horas)")
        opcion = leer_entero_en_rango("Opcion (1-3): ", 1, 3)
        if opcion == 1:
            costo_extra = 150.0
            horas_perdidas_extra = 2.0
            nuevo_estado_maquina = 2        #Nuevo estado:deja la maquina operativa 0% defectos
        elif opcion == 2:
            costo_extra = 40.0
            nuevo_estado_maquina = 1        #Reparación rapida, pero la maquina queda inestable 4%
        else:
            horas_perdidas_extra = 1.5
            nuevo_estado_maquina = 0        # No se interviene, la maquina queda averiada 14%


    # ------------ Jornada 2 -----------------
    elif jornada == 2:
        print("Incidencia: Lote de materia prima con retraso logístico.")
        print("1. Comprar lote local de emergencia (Costo $200, suma 100 kg MP)")
        print("2. Esperar al proveedor (Pierde 3 horas, sin costo)")
        print("3. Trabajar solo con inventario existente (Pierde 1 hora reorganizando el turno)")
        opcion = leer_entero_en_rango("Opcion (1-3): ", 1, 3)
        if opcion == 1:
            costo_extra = 200.0
            mp_extra = 100.0
        elif opcion == 2:
            horas_perdidas_extra = 3.0
        else:
            horas_perdidas_extra = 1.0
        #esta jornada no toca a la maquina, por lo que no se cambia el estado de la misma


    #------------- Jornada 3 -----------------
    elif jornada == 3:
        print("Incidencia: Descalibración de sensores en linea de ensamblaje.")
        print("1. Mantenimiento correctivo especializado (Costo $180, maquina calibrada)")
        print("2. Parar una hora para calibración interna (Pierde 1 hora, maquina queda bien)")
        print("3. Forzar linea sin recalibrar (Maquina averiada)")
        opcion = leer_entero_en_rango("Opcion (1-3): ", 1, 3)
        if opcion == 1:
            costo_extra = 180.0
            nuevo_estado_maquina = 2
        elif opcion == 2:
            horas_perdidas_extra = 1.0
            nuevo_estado_maquina = 2
        else:
            nuevo_estado_maquina = 0


    # ------------ Jornada 4 -----------------
    elif jornada == 4:
        print("Incidencia: Fluctuación de voltaje en la red electrica.")
        print("1. Encender planta electrica secundaria (Costo $120 combustible)")
        print("2. Suspender labores 2 horas por seguridad (Pierde 2 horas)")
        print("3. Asumir el riesgo operativo (Máquina queda vulnerable)")
        opcion = leer_entero_en_rango("Opcion (1-3): ", 1, 3)
        if opcion == 1:
            costo_extra = 120.0
            nuevo_estado_maquina = 2
        elif opcion == 2:
            horas_perdidas_extra = 2.0
            nuevo_estado_maquina = 2
        else:
            nuevo_estado_maquina = 0

    # ------------ Jornada 5 -----------------
    else:
        print("Incidencia: Inspeccion de control de calidad de sorpresa.")
        print("1. Auditoria  detenida (Pierde 2 horas, maquina revisada)")
        print("2. Pago de arancel de certificación urgente (Costo $100)")
        print("3. Continuar operaciones en paralelo (Riesgo de defectos)")
        opcion = leer_entero_en_rango("Opción (1-3): ", 1, 3)
        if opcion == 1:
            horas_perdidas_extra = 2.0
            nuevo_estado_maquina = 2
        elif opcion == 2:
            costo_extra = 100.0
            nuevo_estado_maquina = 2
        else:
            nuevo_estado_maquina = 0

    return costo_extra, horas_perdidas_extra, mp_extra, nuevo_estado_maquina        