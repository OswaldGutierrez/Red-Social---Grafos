import random
import networkx as nx
import matplotlib.pyplot as plt

from NombresComp import generarNombres

def crearRedSocial(cantidad):
    G = nx.Graph()

    for _ in range(cantidad):
        nombreUsuario = generarNombres()
        G.add_node(nombreUsuario)

    minTotalConexiones = 700
    maxTotalConexiones = 1000
    minConexiones = 10
    maxConexiones = 30

    usuarios = list(G.nodes)

    # Generaramos las aristas
    totalConexiones = random.randint(minTotalConexiones, maxTotalConexiones)

    while G.number_of_edges() < totalConexiones:
        u1, u2 = random.sample(usuarios, 2)

        if u1 != u2 and not G.has_edge(u1, u2):
            G.add_edge(u1, u2)

    for usuario in usuarios:
        numConexionesActual = G.degree[usuario]
        numConexionesObjetivo = random.randint(minConexiones, maxConexiones)

        while numConexionesActual < minConexiones:
            otroUsuario = random.choice(usuarios)

            if otroUsuario != usuario and not G.has_edge(usuario, otroUsuario):
                G.add_edge(usuario, otroUsuario)
                numConexionesActual += 1

        while numConexionesActual > maxConexiones:
            vecinos = list(G.neighbors(usuario))
            vecinoEliminar = random.choice(vecinos)
            G.remove_edge(usuario, vecinoEliminar)
            numConexionesActual -= 1

    return G
