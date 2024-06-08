import networkx as nx
import matplotlib.pyplot as plt

def graficarRelacionesComunes(red, nombreUsuario1, nombreUsuario2):
    G = red
    usuarios = list(G.nodes)

    if nombreUsuario1 not in usuarios or nombreUsuario2 not in usuarios:
        print(f"Uno o ambos usuarios no existen en la red social.")
        return

    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G)

    # Obtener vecinos comunes
    vecinosComunes = list(nx.common_neighbors(G, nombreUsuario1, nombreUsuario2))

    # Crear subgrafo con los vecinos comunes y los dos usuarios
    subgrafo = G.subgraph([nombreUsuario1, nombreUsuario2] + vecinosComunes)

    # Dibujar subgrafo
    nx.draw_networkx_nodes(G, pos, nodelist=subgrafo.nodes(), node_color='skyblue', node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=subgrafo.edges(), edge_color='gray', width=1.0, alpha=0.7)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

    plt.title(f"Relaciones comunes entre '{nombreUsuario1}' y '{nombreUsuario2}' en la Red Social")
    plt.axis('off')
    plt.show()
