import json
import networkx as nx
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

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

# Agregar aristas al grafo
for edges in [edges_piso_1, edges_piso_2, edges_piso_3, edges_verticales]:
    G.add_edges_from(edges)

# Posiciones 3D de los nodos
pos = {**nodes_piso_1, **nodes_piso_2, **nodes_piso_3} 

# Generar replicas de nodos y aristas
desplazamiento_z = 3
total_nodes = len(G.nodes())

# Crear las trazas para los nuevos nodos y aristas en Plotly
def create_figure(node_colors):
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

    # listas para agrupar la info sacada del json
    nodes_names = []
    nodes_activities = []
    nodes_lvl_habitability = []

    # Leer el json con la info de los nodos
    with open('Propagacion/objetos/espacios.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        for item in data.items():
            nodes_names.append(item[1]['nombre'])
            nodes_activities.append(item[1]['actividad'])
            nodes_lvl_habitability.append(item[1]['habitabilidad']['nivel_habitabilidad'])

    # Crear texto para la interfaz
    hover_text = [f"Node: {n_node} <br>Nombre: {name} <br>Actividad: {activity} <br>Nivel Habitabilidad: {habitability}" for n_node, name, activity, habitability in zip(G.nodes(), nodes_names, nodes_activities, nodes_lvl_habitability)]

    # Agregar nodos
    fig.add_trace(go.Scatter3d(
        x=node_x, y=node_y, z=node_z,
        mode='markers',
        marker=dict(size=6, color=node_colors),
        text=hover_text,
        hoverinfo='text',
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

    # fig.show()
    return fig

# Crear la app de Dash para poder insertar html
app = dash.Dash(__name__)   

app.layout = html.Div([
    dcc.Graph(id='graph', figure=create_figure(['green'] * len(G.nodes())), style={'height': '80vh'}),
    html.Div(
        children=[
            html.Button('Cambiar Color', id='change-color-button', n_clicks=0,
                        style={
                            'backgroundColor':'#5485ff',
                            'color': 'white', 
                            'border': 'none',
                            'padding': '15px 32px', 
                            'textAlign': 'center',
                            'fontSize': '16px', 
                            'margin': '10px auto', 
                            'cursor': 'pointer',
                            'borderRadius': '12px',
                        })
        ],
        style={'textAlign': 'center', 'padding': '20px'}
    )
])

# Callback que manda el boton para cambiar el color del nodo dinámicamente
@app.callback(
    Output('graph', 'figure'),  # componente que se va a actualizar
    Input('change-color-button', 'n_clicks'), # componente que dispara la actualización
    prevent_initial_call=True
)
# funcion llamada por el boton
def update_color(n_clicks):
    colors = ['green'] * len(G.nodes())
    if n_clicks % 2 == 1:
        colors = ['green', 'red'] * (len(G.nodes())//2)
    return create_figure(colors)

# Correr la app
if __name__ == '__main__':
    app.run_server(debug=True)