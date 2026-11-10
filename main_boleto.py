
from Clases.Boleto import Boleto, BoletoEstudiante, BoletoCortesia

def Menu():
    boletos = [
        Boleto("Andrea", "Sala 2, 18:00"),
        BoletoEstudiante("Bruno", "Sala 2, 18:00"),
        BoletoCortesia("Carla", "Sala 5, 20:30")
    ]

    for boleto in boletos:
        print(boleto.ticket())


Menu()
