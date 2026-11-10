from Clases.Estacionamiento import Estancia, EstanciaPension, EstanciaNocturna

def Menu():
    estancias = [
        Estancia("ABC-123", 3),
        EstanciaPension("XYZ-789"),
        EstanciaNocturna("JKL-456", 5)
    ]

    for estancia in estancias:
        print(estancia.ticket())


Menu()
