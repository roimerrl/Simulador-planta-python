# Modulo de validaciones con try - except que son reutilizables en otros modulos 

def leer_entero_en_rango(mensaje, minimo, maximo):
    """Pide un numero entero y valida que este dentro del minimo y maximo permitido,
      ademas de que sea convertible a int,
      y si falla vuelve a pedir que ingrese el dato."""
    numero = -1
    valido = False
    while not valido:
        try:
            texto = input(mensaje)
            numero = int(texto)
            if numero >= minimo and numero <= maximo:
                valido = True
            else:  # entrada valida pero fuera de rango
                print("Error: Opción fuera de rango. Intente de nuevo.")
        except ValueError:  # entrada diferente a un numero entero
            print("Error: Debe ingresar un número entero valido.")
    return numero

def leer_texto(mensaje):
    """Pide un texto y valida que no este vacio.
    si lo esta vuelve a pedir el dato
    si presiona enter vuelve a pedir el dato"""
    texto = ""
    while texto == "":
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: El texto no puede quedar vacio.")
    return texto