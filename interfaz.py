import networkx as nx
import plotly.graph_objects as go

# Crear el grafo
G = nx.Graph()

# Coordenadas de los nodos por piso
nodes_piso_1 = {
    1:(0,0.75,0), 2:(0,1.25,0), 3:(0,2,0), 4:(0,3,0), 5:(0,4,0),
    6:(1,0.75,0), 7:(1,1.25,0), 8:(1,2,0), 9:(1,3,0), 10:(1.25,3.75,0), 11:(0.75,3.75,0), 12:(1,4.25,0)
}
nodes_piso_2 = {
    13:(0,1,1), 14:(0,2,1), 15:(0,3,1), 16:(0,4,1),
    17:(1,1,1), 18:(1,2,1), 19:(1,3,1), 20:(0.75,4,1), 21: (1,4,1), 22: (1.25,4,1)
}
nodes_piso_3 = {
    23:(0,1,2), 24:(0,2,2), 25:(0,3,2), 26:(0,4,2),
    27:(1,1,2), 28:(1,2,2), 29:(1,3,2), 30:(1,4,2)
}

# Agregar nodos al grafo
for nodes in [nodes_piso_1, nodes_piso_2, nodes_piso_3]:
    G.add_nodes_from(nodes.keys())

# Agregar aristas por piso
edges_piso_1 = [
    (1, 2), (2, 3), (3, 4), (4, 5),
    (6, 7), (7, 8), (8, 9), (9, 10), (9, 11), (10, 11), (10, 12), (11, 12),
]
edges_piso_2 = [
    (13, 14), (14, 15), (15, 16),
    (17, 18), (18, 19), (19, 20), (19, 21), (19, 22), (20, 21), (20, 22),
]
edges_piso_3 = [
    (23, 24), (24, 25), (25, 26),
    (27, 28), (28, 29), (29, 30),
]
# Aristas entre pisos
edges_verticales = [
    (1, 13), (6, 17), (2, 13), (7, 17), (3, 14), (8, 18), (4, 15), (9, 19), (5, 16),
    (10, 22), (11, 21), (12, 20),
    (13, 23), (17, 27), (14, 24), (18, 28), (15, 25), (19, 29), (16, 26),
    (20, 30), (21, 30), (22, 30)
]
edges_verticales_no_replicados = [
    (23,31),(23,32),(27,36),(27,37),
    (24,33),(28,38),(25,34),(29,39),(26,35),
    (30,40),(30,41),(30,42)
]

# Agregar aristas al grafo
for edges in [edges_piso_1, edges_piso_2, edges_piso_3, edges_verticales]:
    G.add_edges_from(edges)

# Posiciones 3D de los nodos
pos = {**nodes_piso_1, **nodes_piso_2, **nodes_piso_3} 

# Crear replica de los pisos 1, 2 y 3
# def replicar_pisos(original_nodes, original_edges, desplazamiento_z, total_nodes):
#     nuevos_nodos = {}
#     nuevos_edges = []
#     nuevo_id = list(G.nodes())[-1]
#     for coords in original_nodes.values():
#         nuevo_id += 1
#         nuevos_nodos[nuevo_id] = (coords[0], coords[1], coords[2] + desplazamiento_z)

#     for edge in original_edges:
#         nuevo_edge = (
#             edge[0] + total_nodes,
#             edge[1] + total_nodes
#         )
#         nuevos_edges.append(nuevo_edge)

#     G.add_nodes_from(nuevos_nodos.keys())
#     G.add_edges_from(nuevos_edges)
#     pos.update(nuevos_nodos)

# def replicar_edges(original_edges, total_nodes):
#     nuevos_edges = []
#     for edge in original_edges:
#         nuevo_edge = (
#             edge[0] + total_nodes,
#             edge[1] + total_nodes
#         )
#         nuevos_edges.append(nuevo_edge)

#     G.add_edges_from(nuevos_edges)

# Generar replicas de nodos y aristas
desplazamiento_z = 3
total_nodes = len(G.nodes())

# replicar_pisos(nodes_piso_1, edges_piso_1, desplazamiento_z, total_nodes)
# replicar_pisos(nodes_piso_2, edges_piso_2, desplazamiento_z, total_nodes)
# replicar_pisos(nodes_piso_3, edges_piso_3, desplazamiento_z, total_nodes)

# replicar_edges(edges_verticales, total_nodes)
# G.add_edges_from(edges_verticales_no_replicados)

# Crear las trazas para los nuevos nodos y aristas en Plotly
edge_x = []
edge_y = []
edge_z = []
for edge in G.edges():
    x0, y0, z0 = pos[edge[0]]
    x1, y1, z1 = pos[edge[1]]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]
    edge_z += [z0, z1, None]

node_x = []
node_y = []
node_z = []
for node in G.nodes():
    x, y, z = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_z.append(z)

# Crear figura con Plotly
fig = go.Figure()

# Agregar aristas
fig.add_trace(go.Scatter3d(
    x=edge_x, y=edge_y, z=edge_z,
    mode='lines',
    line=dict(color='gray', width=2),
    hoverinfo='none'
))

# Agregar nodos
fig.add_trace(go.Scatter3d(
    x=node_x, y=node_y, z=node_z,
    mode='markers',
    marker=dict(size=6, color='green'),
    text=list(G.nodes()),
    hoverinfo='text'
))

# Configurar layout
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='',
        xaxis_visible=False,
        yaxis_visible=False,
        zaxis=dict(showticklabels=False),
        # xaxis=dict(nticks=4),
        # yaxis=dict(nticks=6),
        # zaxis=dict(nticks=4),
    ),
    title='Simulación 3D, Habitabilidad y propagación de Luz, basado en el Edificio Techné UD, 6 Pisos',
    showlegend=False
)

fig.show()
