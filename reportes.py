""" modulo de reportes.py
responsable de mostrar por pantalla el estado de la planta, evaluar cada
jornada y armar el informe final. Aqui no se hacen calculos de produccion,
solo se reciben datos ya calculados desde main.py y se imprimen ordenados
"""
from mantenimiento import descripcion_estado_maquina

def mostrar_panel_estado(plan, realizada, pendiente, materiaprima, desperdicio, h_disp, h_util, h_perd, defectuoso, calidad, costo,
eficiencia, cumplimiento, estado_maq):
    # El estado de la maquina se guarda como numero, pero se muestra como texto
    print("\n=========================================")
    print("           ESTADO DE LA PLANTA           ")
    print("=========================================")
    # Se usa formato .2f en los decimales para que las columnas queden alineadas y bonitas
    print(f"Produccion planificada: {plan}")
    print(f"Produccion realizada  : {realizada}")
    print(f"Produccion pendiente  : {pendiente}")
    print(f"Materia prima          : {materiaprima:.2f} kg")
    print(f"Desperdicio            : {desperdicio:.2f} kg")
    print(f"Horas disponibles      : {h_disp:.2f} h")
    print(f"Horas utilizadas       : {h_util:.2f} h")
    print(f"Horas perdidas         : {h_perd:.2f} h")
    print(f"Productos defectuosos : {defectuoso}")
    print(f"Calidad                : {calidad:.2f}%")
    print(f"Cumplimiento           : {cumplimiento:.2f}%")
    print(f"Costo acumulado        : ${costo:.2f}")
    print(f"Eficiencia             : {eficiencia:.2f}%")
    print(f"Estado de la planta    : {descripcion_estado_maquina(estado_maq)}")
    print("=========================================\n")

# Funcion explicita para el control de calidad 
def evaluar_calidad(porcentaje_calidad):
    """Devuelve el nivel de calidad segun los criterios definidos por el equipo:
       - Calidad >= 95%  -> Aceptable
       - Calidad 90-94%  -> Atencion
       - Calidad < 90%   -> Critico
    95% es el estandar industrial minimo para considerar un plan exitoso,
    y 90% es el limite de tolerancia antes de considerar el lote como critico
    """
    if porcentaje_calidad >= 95.0:
        return "Aceptable"
    elif porcentaje_calidad >= 90.0:
        return "Atencion"
    else:
        return "Critico"

# funcion solo para evaluar el estado de la jornada
def evaluar_jornada(realizada, plan, calidad, materiaprima, h_disp):
    """Evalua el estado de la jornada segun cumplimiento, calidad y recursos.
    Devuelve uno de los 5 estados definidos por el equipo:
       - JORNADA SUPERADA
       - CUMPLIDA CON OBSERVACIONES
       - PRODUCCION EN RIESGO
       - RECURSOS INSUFICIENTES
       - JORNADA CRITICA / NO CUMPLIDA
    """
    nivel = evaluar_calidad(calidad)
    print("ESTADO DE LA JORNADA")
    print(f"Nivel de calidad: {nivel}")

    # Caso 1: recursos insuficientes (materiaprima o horas agotadas)
    if materiaprima <= 0 or h_disp <= 0:
        print("Resultado : RECURSOS INSUFICIENTES")
        print("--------------------------------------")
        return

    # Caso 2: calidad critica
    if nivel == "Critico":
        print("Resultado : JORNADA CRITICA / NO CUMPLIDA")
        print("---------------------------------------")
        return

    # Caso 3: jornada superada (cumplio y calidad aceptable)
    if realizada >= plan and nivel == "Aceptable":
        print("Resultado : JORNADA SUPERADA")
    # Caso 4: cumplida con observaciones (cumplio pero calidad en atencion)
    elif realizada >= plan and nivel == "Atencion":
        print("Resultado : JORNADA CUMPLIDA CON OBSERVACIONES")
    # Caso 5: produccion en riesgo (no cumplio pero calidad no es critica)
    elif realizada < plan:
        print("Resultado : PRODUCCION EN RIESGO (Incompleta)")
    else:
        print("Resultado : JORNADA NO CUMPLIDA")
    print("-----------------------------------------")


def mostrar_informe_final(plan_total, real_total, def_total, desp_total,h_util_total, h_perd_total, costo_total,
mp_final, estado_final, h_total_inicial):
    """esta es para mostrar el informe final consolidado de las 5 jornadas.
    Recibe la materia prima final y el estado final de la maquina para mostrarlos
    y poder determinar el resultado critico por falta de recursos."""
    # Los porcentajes se calculan aqui mismo para no tener que pasarlos como parametros
    cumplimiento = 0.0
    if plan_total > 0:
        cumplimiento = (real_total / plan_total) * 100.0

    # Calidad: si no se produjo nada, es 0% (no hay calidad que medir)
    calidad_total = 0.0
    if real_total > 0:
        calidad_total = ((real_total - def_total) / real_total) * 100.0

    eficiencia_final = (cumplimiento + calidad_total) / 2.0

    pendiente_total = plan_total - real_total
    if pendiente_total < 0:
        pendiente_total = 0

    # Horas restantes al final de la simulacion
    horas_restantes = h_total_inicial - h_util_total - h_perd_total

    print("\n=========================================")
    print("              INFORME FINAL              ")
    print("=========================================")
    print(f"Produccion planificada : {plan_total}")
    print(f"Produccion realizada   : {real_total}")
    print(f"Produccion pendiente   : {pendiente_total}")
    print(f"Total defectuosos      : {def_total}")
    print(f"Cumplimiento           : {cumplimiento:.1f}%")
    print(f"Calidad                : {calidad_total:.1f}% ({evaluar_calidad(calidad_total)})")
    print(f"Desperdicio acumulado  : {desp_total:.1f} kg")
    print(f"Horas utilizadas       : {h_util_total:.1f} h")
    print(f"Horas perdidas         : {h_perd_total:.1f} h")
    print(f"Horas restantes        : {horas_restantes:.1f} h")
    print(f"Materia prima restante : {mp_final:.1f} kg")
    print(f"Estado final maquina   : {descripcion_estado_maquina(estado_final)}")
    print(f"Eficiencia final       : {eficiencia_final:.1f}%")
    print(f"Costo final            : ${costo_total:.2f}")
    print("---------------------------------------")


    # Orden: primero recursos,  calidad, luego cumplimiento
    if mp_final <= 0 or horas_restantes <= 0:
        print("RESULTADO: CRITICO POR FALTA DE RECURSOS")
    elif calidad_total < 90.0:
        print("RESULTADO: CRITICO POR PROBLEMAS DE CALIDAD")
    elif cumplimiento >= 95.0 and calidad_total >= 95.0:
        print("RESULTADO: CUMPLIMIENTO SATISFACTORIO DEL PLAN")
    elif cumplimiento >= 80.0:
        print("RESULTADO: CUMPLIMIENTO PARCIAL")
    else:
        print("RESULTADO: INCUMPLIMIENTO DEL PLAN")
    print("=========================================\n")
