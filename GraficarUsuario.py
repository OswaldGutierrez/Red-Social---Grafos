from CrearRedSocial import crearRedSocial
from MenuRedSocial import mostrarMenu
from NombresComp import generarNombres
import networkx as nx
import matplotlib.pyplot as plt

def graficarRelacionesUsuario(red, nombreUsuario):
    G = red
    usuarios = list(G.nodes)

    if nombreUsuario not in usuarios:
        print(f"El usuario '{nombreUsuario}' no existe en la red social.")
        return

    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G)

    subgrafo = nx.ego_graph(G, nombreUsuario, radius=1)

    # Dibujamos el subgrafo
    nx.draw_networkx_nodes(G, pos, nodelist=subgrafo.nodes(), node_color='skyblue', node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=subgrafo.edges(), edge_color='gray', width=1.0, alpha=0.7)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

    plt.title(f"Relaciones de '{nombreUsuario}' en la Red Social")
    plt.axis('off')
    plt.show()