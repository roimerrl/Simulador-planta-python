def planificar_jornada(meta_producir, materiadisp, horasdisp, estado_maquina):
    if estado_maquina == 0:
        print("aviso de planta: maquinaria con fallas")
    
    #gasta 1 kg de materia y 0.03 horas
    posibles_m = int(materiadisp / 1.0)
    posibles_hr = int(horasdisp / 0.03)
    
    producto = meta_producir
    
    if producto > posibles_m:
        producto = posibles_m
    if producto > posibles_hr:
        producto = posibles_hr
        
    return producto


def calcular_consumo(unidades_producidas):
    #para saber cuanto material y horas se usaron
    mp_consumida = unidades_producidas * 1.0
    horas_utilizadas = unidades_producidas * 0.03
    return mp_consumida, horas_utilizadas


def calcular_defectos_y_desperdicio(unidades_producidas, estado_maquina):
    # 0 = averiada (14%), 1 = operativa normal / ajuste rapido (4%), 2 = optima (0%)
    #calculo de fallas 
    if estado_maquina == 2:
        tasa = 0.0
    elif estado_maquina == 1:
        tasa = 0.04
    else:
        tasa = 0.14
        
    defectos = int(unidades_producidas * tasa)
    desperdicio = defectos * 0.75
    return defectos, desperdicio


def calcular_costo_operativo(mp_consumida, H_utilizadas, H_perdidas, defectos):
    # costos totales
    mp_temp = float(mp_consumida)
    c1 = mp_temp * 5.0
    c2 = H_utilizadas * 10.0
    c3 = H_perdidas * 15.0
    c4 = defectos * 2.0
    costo = c1 + c2 + c3 + c4
    return costo
