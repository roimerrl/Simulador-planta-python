""" Modulo  main.py
es el archivo principal que une todo y hace el ciclo de las 5 jornadas
flujo de cada jornada :
Mantenimiento -> Planificacion -> Produccion -> Incidencia -> Decision -> Actualizacion -> Control -> Reporte"""

from validaciones import leer_entero_en_rango
from configuracion import (bienvenida, seleccionar_escenario, inicializar_materia_prima,
inicializar_horas, inicializar_meta_jornada, mostrar_parametros_iniciales)
from produccion import (planificar_jornada, calcular_consumo, calcular_defectos_y_desperdicio,calcular_costo_operativo, calcular_calidad, calcular_cumplimiento,
calcular_eficiencia, calcular_produccion_pendiente)
from incidencias import aplicar_incidencia
from reportes import mostrar_panel_estado, evaluar_jornada, mostrar_informe_final
from mantenimiento import evaluar_mantenimiento, realizar_mantenimiento

def simular_produccion():
    nombre_planta, supervisor = bienvenida()
    escenario = seleccionar_escenario()

    # Valores iniciales
    materia_prima = inicializar_materia_prima(escenario)
    horas_totales = inicializar_horas(escenario)
    meta_diaria = inicializar_meta_jornada(escenario)

    # mostramos los parametros iniciales para que el usuario sepa con que arranca
    mostrar_parametros_iniciales(nombre_planta, supervisor, escenario, materia_prima, horas_totales, meta_diaria)

    # Variables globales para el informe final
    total_planificado = 0
    total_realizado = 0
    total_defectos = 0
    total_desperdicio = 0.0
    total_horas_utilizadas = 0.0
    total_horas_perdidas = 0.0
    costo_acumulado = 0.0
    estado_maquina = 2  # 2 = optima, 1 = operativa, 0 = averiada

    # Guardamos las horas totales originales para el informe final
    horas_totales_inicial = horas_totales

    # Hacemos el ciclo para 5 jornadas
    for jornada in range(1, 6):
        print(f"\n================ JORNADA {jornada} DE 5 ================")
        print(f"Planta: {nombre_planta} | Supervisor: {supervisor}")

        # 0. Mantenimiento (se ofrece en TODAS las jornadas porsia porsia)
        tipo_mant = evaluar_mantenimiento(estado_maquina, jornada)
        horas_mant = 0.0
        print("\n--- DEPARTAMENTO DE MANTENIMIENTO ---")
        if tipo_mant == 2:
            print("La máquina está averiada. Se requiere mantenimiento correctivo.")
            print("  Costo: $200, Tiempo: 2.0 h. Deja la máquina óptima.")
        else:
            print("Se ofrece mantenimiento preventivo para conservar el estado de la máquina.")
            print("  Costo: $80, Tiempo: 1.0 h. Deja la máquina óptima.")

        print("¿Desea realizar el mantenimiento?")
        print("1. Sí (Aplica el mantenimiento sugerido)")
        print("2. No (Omitir)")
        opc_mant = leer_entero_en_rango("Opción (1-2): ", 1, 2)

        if opc_mant == 1:
            costo_mant, horas_mant, estado_maquina = realizar_mantenimiento(tipo_mant, estado_maquina)
            costo_acumulado = costo_acumulado + costo_mant
            total_horas_perdidas = total_horas_perdidas + horas_mant
            horas_totales = horas_totales - horas_mant  # se descuenta del pool total
            print(f">> Mantenimiento aplicado. Costo: ${costo_mant}, Horas perdidas: {horas_mant} h")
        else:
            print(">> Mantenimiento omitido por el supervisor.")

        """1. Planificacion
         Calculamos las horas disponibles para esta jornada
         broimportante: las horas perdidas en incidencias anteriores YA se restaron de horas_totales,
         asi que aqui solo repartimos lo que queda entre las jornadas restantes.
         Si horas_totales ya es <= 0, no hay horas para producir nada"""

        jornadas_restantes = 6 - jornada  # van 1,2,3,4,5 -> restantes 5,4,3,2,1
        if horas_totales <= 0.0:
            horas_turno = 0.0
            print(">> AVISO: No hay horas disponibles. La planta no puede producir esta jornada.")
        else:
            horas_turno = (horas_totales / jornadas_restantes)

        unidades_turno, alerta_plan = planificar_jornada(meta_diaria, materia_prima, horas_turno, estado_maquina)
        if alerta_plan != "":
            print(alerta_plan)
        if estado_maquina == 0:
            print("! Aviso de Planta: Maquinaria averiada, capacidad reducida al 50%.")

        total_planificado = total_planificado + meta_diaria

        # 2. Producción
        mp_usada, horas_usadas = calcular_consumo(unidades_turno)
        defectos_turno, desp_turno = calcular_defectos_y_desperdicio(unidades_turno, estado_maquina)

        total_horas_utilizadas = total_horas_utilizadas + horas_usadas
        total_realizado = total_realizado + unidades_turno
        total_defectos = total_defectos + defectos_turno
        total_desperdicio = total_desperdicio + desp_turno

        # 3. Incidencia y Decisión
        costo_extra, horas_perd, mp_extra, estado_maquina = aplicar_incidencia(jornada, estado_maquina)

        # 4. Actualización de variables
        materia_prima = materia_prima + mp_extra - mp_usada
        costo_acumulado = costo_acumulado + costo_extra
        total_horas_perdidas = total_horas_perdidas + horas_perd
        horas_totales = horas_totales - horas_perd  # se descuenta del pool total
        horas_totales = horas_totales - horas_usadas  # las horas usadas tambien se descuentan

        # 5. Costo operativo del turno
        costo_turno = calcular_costo_operativo(mp_usada, horas_usadas, horas_mant + horas_perd, defectos_turno)
        costo_acumulado = costo_acumulado + costo_turno

        # 6. Control e indicadores
        calidad_turno = calcular_calidad(unidades_turno, defectos_turno)
        cumplimiento_turno = calcular_cumplimiento(unidades_turno, meta_diaria)
        eficiencia_turno = calcular_eficiencia(cumplimiento_turno, calidad_turno)
        pendiente_turno = calcular_produccion_pendiente(meta_diaria, unidades_turno)

        # 7. Reportes
        mostrar_panel_estado(meta_diaria, unidades_turno, pendiente_turno, materia_prima,
        desp_turno, horas_totales, horas_usadas, horas_mant + horas_perd,
        defectos_turno, calidad_turno, costo_acumulado, eficiencia_turno,cumplimiento_turno, estado_maquina)
        evaluar_jornada(unidades_turno, meta_diaria, calidad_turno, materia_prima, horas_totales)

    # Fuera del ciclo, mostramos el balance de las 5 jornadas
    mostrar_informe_final(total_planificado, total_realizado, total_defectos,total_desperdicio, total_horas_utilizadas,
    total_horas_perdidas, costo_acumulado,materia_prima, estado_maquina, horas_totales_inicial)

def main():
    # Bucle para repetir el simulador sin salirse
    repetir = 1
    while repetir == 1:
        simular_produccion()
        print("¿Desea realizar otra simulación?")
        print("1. Si")
        print("2. No")
        repetir = leer_entero_en_rango("Ingrese su opción: ", 1, 2)
    print("\nSimulación finalizada. ¡Hasta luego!")

main()
