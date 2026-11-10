"""Modulo de mantenimiento.py
es el encargado de la gestion del mantenimiento de la maquinaria
Estado de la maquina: 2 = optima, 1 = operativa (con desgaste), 0 = averiada
"""
# costos y tiempos de mantenimiento (constantes para facilitar cambios en la defensa)
COSTO_PREVENTIVO = 80.0
TIEMPO_PREVENTIVO = 1.0
COSTO_CORRECTIVO = 200.0
TIEMPO_CORRECTIVO = 2.0


def evaluar_mantenimiento(estado_maquina, jornada):
    """Decide qué tipo de mantenimiento se le ofrece al usuario en cada jornada.
    se pone en duda si se el usuario puede decidir si hace o no
    mantenimiento en cualquier momento, asi que se ofrece todos los dias

    - Si la maquina esta averiada (0): ofrece mantenimiento correctivo.
    - Si la maquina esta operativa (1) u optima (2): ofrece mantenimiento preventivo.

    Devuelve:
      2 = mantenimiento correctivo sugerido
      1 = mantenimiento preventivo sugerido
    """
    if estado_maquina == 0:
        return 2
    return 1


def realizar_mantenimiento(tipo, estado_actual):
    """Aplica el mantenimiento segun el tipo.
    tipo 1 = Preventivo, tipo 2 = Correctivo.
    Devuelve (costo, horas_perdidas, nuevo_estado).
    No imprime nada: los mensajes los muestra main.py para mantener la separacion
    de responsabilidades.
    """
    costo = 0.0
    horas_perdidas = 0.0
    nuevo_estado = estado_actual

    if tipo == 2:
        # mantenimiento correctivo: arregla maquina averiada, la deja optima
        costo = COSTO_CORRECTIVO
        horas_perdidas = TIEMPO_CORRECTIVO
        nuevo_estado = 2
    elif tipo == 1:
        # mantenimiento preventivo: mantiene la maquina en estado optimo
        costo = COSTO_PREVENTIVO
        horas_perdidas = TIEMPO_PREVENTIVO
        nuevo_estado = 2

    return costo, horas_perdidas, nuevo_estado


def descripcion_estado_maquina(estado):
    """devuelve un texto legible del estado de la maquina para los reportes"""
    if estado == 2:
        return "Optima"
    elif estado == 1:
        return "Operativa"
    else:
        return "Con fallas"
