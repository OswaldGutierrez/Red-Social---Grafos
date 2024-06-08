def mostrarMenu():
    while True:
        try:
            numUsuarios = int(input("¿Cuántos usuarios quiere que tenga su red social? (Mínimo 100, máximo 500): "))
            if 100 <= numUsuarios <= 500:
                return numUsuarios
            else:
                print("Por favor, ingrese un número entre 100 y 500.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")