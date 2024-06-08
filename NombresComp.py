import random

primerNombres = [
    "Oswald", "David", "Daniel", "Leonard", "Robert", "Iván", "Juan", "Andrés", "Álvaro", "Antonio", "José", "Jhoandry", "Daniela", "Norleivys", "María", "Carmen",
    "Liceth", "Jesús", "Enzo", "Ángel", "Ángeles", "Óscar", "Alberto", "Diana", "Enrique", "Nicoll", "Alex", "Alexey", "Jaime", "Lina", "Jeremy"
]
segundoNombres = [
    "Luz", "Alejandra", "Laura", "Felipe", "Rafael", "Katy", "Tobías", "Marina", "Mary", "Deila", "Alexis", "Margarita", "Northon", "Ángela", "Natalia", "Valentina",
     "Valeria", "Manuel", "Diego", "Augusto", "Pablo", "Jose", "Samuel", "Ana", "Joan", "Kevin", "Sofi", "Julio", "Wilmer", "Dubán", "Raquel", "Smith", "Nicolás"
]

nombresGenerados = set()

def generarNombres():
    while True:
        primerNombre = random.choice(primerNombres)
        segundoNombre = random.choice(segundoNombres)
        nombreCompuesto = f"{primerNombre} {segundoNombre}"
        if nombreCompuesto not in nombresGenerados:
            nombresGenerados.add(nombreCompuesto)
            return nombreCompuesto