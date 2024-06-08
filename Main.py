from CrearRedSocial import crearRedSocial
from MenuRedSocial import mostrarMenu
import networkx as nx
import matplotlib.pyplot as plt
from GraficarUsuario import graficarRelacionesUsuario
from RelacionesComunes import graficarRelacionesComunes

def main():
    numUsuarios = mostrarMenu()
    redSocial = crearRedSocial(numUsuarios)

    print(f"Red social creada con {numUsuarios} usuarios.")

    # Graficar la red completa
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(redSocial)
    nx.draw(redSocial, pos, with_labels=True, node_size=50, node_color='skyblue', font_size=8, font_color='black', font_weight='bold')
    plt.show()

    while True:
        print("\n1. Ver relaciones de un usuario específico.")
        print("2. Ver relaciones comunes entre dos usuarios.")
        print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            nombreUsuario = input("Ingrese el nombre del usuario para ver sus relaciones (o 'salir' para terminar): ").strip()
            if nombreUsuario.lower() == 'salir':
                break
            graficarRelacionesUsuario(redSocial, nombreUsuario)

        elif opcion == '2':
            nombreUsuario1 = input("Ingrese el nombre del primer usuario para ver relaciones en común: ").strip()
            nombreUsuario2 = input("Ingrese el nombre del segundo usuario para ver relaciones en común: ").strip()
            graficarRelacionesComunes(redSocial, nombreUsuario1, nombreUsuario2)

        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
