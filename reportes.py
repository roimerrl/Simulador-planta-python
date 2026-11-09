# Modulo: reportes.py
# Autores: Roimer
# Resposable de mostrar por pantalla el estado de la planta, evaluar cada
# jornada y armar el informe final. Aqui no se hacen calculos de produccion,
# solo se reciben datos ya calculados desde main.py y se imprimen ordenados

def mostrar_panel_estado(plan, realizada, pendiente, materiaprima, desperdicio, h_disp, h_util, h_perd, defectuoso, calidad, costo, eficiencia, estado_maq):
    # El estado de la maquina se guarda como 1 o 0, pero al usuario hay que
    # mostrarle algo legible, por eso se convierte a texto antes de imprimir
    if estado_maq == 2:
        texto_maq = "Optima"
    elif estado_maq == 1:
        texto_maq = "Operativa"
    else:
        texto_maq = "Con fallas"
        
    print("\n=========================================")
    print("           ESTADO DE LA PLANTA           ")
    print("=========================================")
    # Se usa formato .2f en los decimales para que las columnas queden alineadas
    print(f"Produccion planificada: {plan}")
    print(f"Produccion realizada  : {realizada}")
    print(f"Produccion pendiente  : {pendiente}")
    print(f"Materia prima         : {materiaprima:.2f} kg")
    print(f"Desperdicio           : {desperdicio:.2f} kg")
    print(f"Horas disponibles     : {h_disp:.2f} h")
    print(f"Horas utilizadas      : {h_util:.2f} h")
    print(f"Horas perdidas        : {h_perd:.2f} h")
    print(f"Productos defectuosos : {defectuoso}")
    print(f"Calidad               : {calidad:.2f}%")
    print(f"Costo acumulado       : ${costo:.2f}")
    print(f"Eficiencia            : {eficiencia:.2f}%")
    print(f"Estado de la planta   : {texto_maq}")
    print("=========================================\n")

def evaluar_jornada(realizada, plan, calidad):
    #Reglas del equipo para decidir si la jornada se supero o no:
    # - Si cumple el plan y la calidad es >= 90% => superada
    # - Si no cumple el plan pero la calidad esta bien => incompleta
    # - Si la calidad es < 90% => critica por defectos
    # - Cualquier otro caso raro => no cumplida
    # TODO: revisar si conviene subir el umbral de calidad a 92% cuando
    # la maquina viene con fallas de la jornada anterior
    print("ESTADO DE LA JORNADA")
    if realizada >= plan and calidad >= 90.0:
        print("Resultado : JORNADA SUPERADA")
    elif realizada < plan and calidad >= 90.0:
        print("Resultado : PRODUCCION INCOMPLETA (Falta de tiempo o material)")
    elif calidad < 90.0:
        print("Resultado : JORNADA CRITICA POR DEFECTOS")
    else:
        print("Resultado : JORNADA NO CUMPLIDA")
    print("-----------------------------------------")

def mostrar_informe_final(plan_total, real_total, def_total, desp_total, h_util_total, h_perd_total, costo_total):
    #Los porcentajes se calculan aqui mismo para no tener que pasarlos como parametros desde main.py para que la funcion solo recibe los totales
    cumplimiento = 0.0
    if plan_total > 0:
        cumplimiento = (real_total / plan_total) * 100.0
        
    #si no se produjo nada, se asume calidad 100% para no dividir entre 0
    calidad_total = 100.0
    if real_total > 0:
        calidad_total = ((real_total - def_total) / real_total) * 100.0
        
    #eficiencia final = promedio simple entre cumplimiento y calidad
    eficiencia_final = (cumplimiento + calidad_total) / 2.0
    
    #el pendiente no puede ser negativo (por si se produjo de mas)
    pendiente_total = plan_total - real_total
    if pendiente_total < 0:
        pendiente_total = 0
    
    print("\n=========================================")
    print("              INFORME FINAL              ")
    print("=========================================")
    print(f"Produccion planificada : {plan_total}")
    print(f"Produccion realizada   : {real_total}")
    print(f"Produccion pendiente   : {pendiente_total}")
    print(f"Total defectuosos      : {def_total}")
    print(f"Cumplimiento           : {cumplimiento:.1f}%")
    print(f"Calidad                : {calidad_total:.1f}%")
    print(f"Desperdicio acumulado  : {desp_total:.1f} kg")
    print(f"Horas utilizadas       : {h_util_total:.1f} h")
    print(f"Horas perdidas         : {h_perd_total:.1f} h")
    print(f"Eficiencia final       : {eficiencia_final:.1f}%")
    print(f"Costo final            : ${costo_total:.2f}")
    print("=========================================\n")
    
    # se va a mostrar en una version posterior, por ahora esta funcion solo imprime los nmeros
