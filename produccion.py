""" Modulo: produccion.py
 Se establecen reglas matemáticas de la planta, consumos, defectos, costos e indicadores
 También guardo por aquí todas las constantes y reglas del negocio 
para no tener que números por todo el código."""


MP_POR_UNIDAD = 1.0          # kg de materia prima por unidad producida
HORAS_POR_UNIDAD = 0.03      # horas de trabajo por unidad producida
TASA_DEFECTOS_OPTIMA = 0.00  # 0% cuando la maquina esta optima (estado 2)
TASA_DEFECTOS_OPERATIVA = 0.04  # 4% cuando la maquina esta operativa normal (estado 1)
TASA_DEFECTOS_AVERIADA = 0.14   # 14% cuando la maquina esta averiada (estado 0)
COSTO_MP = 5.0               # $ por kg de materia prima consumida
COSTO_HORA_USADA = 10.0      # $ por hora de trabajo utilizada
COSTO_HORA_PERDIDA = 15.0    # $ por hora perdida (penalizacion)
COSTO_DEFECTO = 2.0          # $ por cada pieza defectuosa

""" Factor de capacidad productiva segun el estado de la máquina
 (estado 2 = optima, 1 = operativa con desgaste, 0 = averiada)"""
FACTOR_CAPACIDAD_OPTIMA = 1.0      # 100% de capacidad
FACTOR_CAPACIDAD_OPERATIVA = 0.90  # 90% de capacidad (desgaste normal)
FACTOR_CAPACIDAD_AVERIADA = 0.50   # 50% de capacidad (maquina averiada produce lento)


def planificar_jornada(meta_producir, materiadisp, horasdisp, estado_maquina):
    """ Calcula cuantas unidades se pueden producir según la meta, MP y horas.
     El estado de la máquina afecta la capacidad productiva:
       - optima (2): 100% capacidad
       - operativa (1): 90% capacidad (desgaste normal)
       - averiada (0): 50% capacidad (produce lento)
     Devuelve (unidades_posibles, alerta) donde alerta es un string con avisos."""
    
    if estado_maquina == 2:
        factor = FACTOR_CAPACIDAD_OPTIMA
    elif estado_maquina == 1:
        factor = FACTOR_CAPACIDAD_OPERATIVA
    else:
        factor = FACTOR_CAPACIDAD_AVERIADA
    
    #gasta 1 kg de materia y 0.03 horas
    posibles_m = int(materiadisp / MP_POR_UNIDAD)
    posibles_hr = int(horasdisp / HORAS_POR_UNIDAD)

    # Aplicamos el factor de capacidad al maximo posible segun las horas
    posibles_hr_ajustado = int(posibles_hr * factor)

    producto = meta_producir
    alerta = ""


    # Generamos alertas si no se puede cumplir la meta
    if producto > posibles_m:
        producto = posibles_m
        alerta = "ADVERTENCIA: Materia prima insuficiente. Plan ajustado a " + str(producto) + " unidades."

    elif producto > posibles_hr_ajustado:
        producto = posibles_hr_ajustado
        if estado_maquina == 0:
            alerta = "ADVERTENCIA: Maquina averiada (50% capacidad). Plan ajustado a " + str(producto) + " unidades."
        elif estado_maquina == 1:
            alerta = "ADVERTENCIA: Maquina operativa con desgaste (90% capacidad). Plan ajustado a " + str(producto) + " unidades."
        else:
            alerta = "ADVERTENCIA: Horas insuficientes. Plan ajustado a " + str(producto) + " unidades."

    if producto < 0:
        producto = 0

    return producto, alerta


def calcular_consumo(unidades_producidas):
    #para saber cuanto material y horas se usaron
    mp_consumida = unidades_producidas * MP_POR_UNIDAD
    horas_utilizadas = unidades_producidas * HORAS_POR_UNIDAD
    return mp_consumida, horas_utilizadas


def calcular_defectos_y_desperdicio(unidades_producidas, estado_maquina):
    # 0 = averiada (14%), 1 = operativa normal / ajuste rapido (4%), 2 = optima (0%)
    #calculo de fallas 
    if estado_maquina == 2:
        tasa = TASA_DEFECTOS_OPTIMA
    elif estado_maquina == 1:
        tasa = TASA_DEFECTOS_OPERATIVA
    else:
        tasa = TASA_DEFECTOS_AVERIADA
        
    defectos = int(unidades_producidas * tasa)
    desperdicio = defectos * 0.75
    return defectos, desperdicio


def calcular_costo_operativo(mp_consumida, H_utilizadas, H_perdidas, defectos):
    # costos totales del turno
    mp_temp = float(mp_consumida)
    c1 = mp_temp * COSTO_MP
    c2 = H_utilizadas * COSTO_HORA_USADA
    c3 = H_perdidas * COSTO_HORA_PERDIDA
    c4 = defectos * COSTO_DEFECTO
    costo = c1 + c2 + c3 + c4
    return costo


# Funciones explicitas para calcular indicadores
def calcular_calidad(unidades_producidas, defectos):
    # Si no se produjo nada, la calidad es 0% (no se puede medir calidad sin produccion)
    if unidades_producidas > 0:
        return ((unidades_producidas - defectos) / unidades_producidas) * 100.0
    return 0.0

def calcular_cumplimiento(realizada, planificada):
    if planificada > 0:
        return (realizada / planificada) * 100.0
    return 0.0

def calcular_eficiencia(cumplimiento, calidad):
    # Eficiencia ponderada 50% cumplimiento, 50% calidad
    return (cumplimiento * 0.5) + (calidad * 0.5)

def calcular_produccion_pendiente(meta, realizada):
    # Cuantas unidades faltaron para cumplir la meta
    pendiente = meta - realizada
    if pendiente < 0:
        pendiente = 0
    return pendiente
