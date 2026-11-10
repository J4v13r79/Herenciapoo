
from Clases.Boleto import Boleto, BoletoEstudiante, BoletoCortesia, BoletoTerceraEdad

def Menu():
    boletos = [
        Boleto("Andrea", "Sala 2, 18:00"),
        BoletoEstudiante("Bruno", "Sala 2, 18:00"),
        BoletoCortesia("Carla", "Sala 5, 20:30"),
        BoletoTerceraEdad("Diana", "Sala 1, 16:00")
    ]

    for boleto in boletos:
        print(boleto.ticket())


Menu()

