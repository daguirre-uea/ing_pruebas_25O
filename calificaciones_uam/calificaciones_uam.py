def calificacion(puntaje):
    # Lanzar exception de tipo
    if not isinstance(puntaje, (int, float)):
        raise TypeError(f"El puntaje debe ser int o float, se recibió {type(puntaje).__name__}")
    
    if 9 <= puntaje <= 10:
        return "A"
    elif 7.5 <= puntaje < 9:
        return "B"
    elif 6 <= puntaje < 7.5:
        return "S"
    elif 0 <= puntaje < 6:
        return "NA"
    else:
        #Lanzar una excepción de valor
        raise ValueError(f"El puntaje está fuera de rango, se recibió {puntaje}")