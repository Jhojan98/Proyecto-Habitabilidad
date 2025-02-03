import json
import networkx as nx
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from modelado.classEdificio import Edificio

# ------ OBTENCION DE DATOS ------
# Variables globales
nodes_colors = []
colors_time = ['white', 'black', '#e3e6ff']
is_night = False  # False = día, True = noche
edificio = Edificio.cargar_desde_json('objetos/edificio.json')
# Leer el json y obtener los datos de los espacios
def get_data():
    global edificio
    return [f"""Node: {n_node} 
            <br>Nombre: {habitacion.nombre} 
            <br>Actividad: {habitacion.actividad.nombre} 
            <br>Nivel Habitabilidad: {habitacion.habitabilidad.nivel_habitabilidad}""" 
            for n_node, habitacion
            in zip(G.nodes(), edificio.habitaciones.values())]  # Usar .values() aquí

# ------ CREACION DEL GRAFO ------
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

    # Agregar nodos
    fig.add_trace(go.Scatter3d(
        x=node_x, y=node_y, z=node_z,
        mode='markers',
        marker=dict(size=6, color=node_colors),
        text=get_data(),
        hoverinfo='text',
    ))

    # Configurar layout
    fig.update_layout(
        paper_bgcolor= colors_time[0],  
        font_color=colors_time[1], 
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='',
            xaxis_visible=False,
            yaxis_visible=False,
            # zaxis_visible=False,
            zaxis=dict(showgrid=False, showticklabels=False, zeroline=False, backgroundcolor=colors_time[2]),
            # xaxis=dict(nticks=4),
            # yaxis=dict(nticks=6),
            # zaxis=dict(nticks=4),
        ),
        title='Simulación 3D, Habitabilidad y propagación de Luz, basado en el Edificio Techné UD, 3 Pisos',
        showlegend=False
    )

    # fig.show()
    return fig

# ------ BOTONES Y LLAMADO DE FUNCIONES  ------
# Crear la app de Dash para poder insertar html
app = dash.Dash(__name__)   

button_style = {
    'backgroundColor':'#5485ff',
    'color': 'white', 
    'border': 'none',
    'padding': '15px 32px', 
    'textAlign': 'center',
    'fontSize': '16px', 
    'margin': '10px 10px', 
    'cursor': 'pointer',
    'borderRadius': '12px',
}

app.layout = html.Div([
        dcc.Location(id='url', refresh=True),  # Añadir dcc.Location
        dcc.Graph(id='graph', figure=create_figure(['blue'] * len(G.nodes())), style={'height': '80vh'}),
        html.Div(
            children=[
                html.Button('Recalcular habitabilidad', id='change-color-button', n_clicks=0, style=button_style),
                html.Button('Cambiar tiempo', id='change-time', n_clicks=0, style=button_style)
            ],
            style={'textAlign': 'center', 'padding': '20px'}
        )
    ]
)

# Callback que manda el boton para cambiar el color del nodo dinámicamente
@app.callback(
    Output('graph', 'figure', allow_duplicate=True), # componente que se va a actualizar
    Input('change-color-button', 'n_clicks'), # componente que dispara la actualización
    prevent_initial_call=True
)

# funcion llamada por el boton
def update_color(n_clicks):
    edificio.calcular_habitabilidad(is_night)
    nodes_colors.clear()

    for habitacion in edificio.habitaciones.values():
        lvl_habitability = habitacion.habitabilidad.nivel_habitabilidad
        if lvl_habitability == 50:
            nodes_colors.append('red')
        elif lvl_habitability == 75:
            nodes_colors.append('orange')
        else:  # 100
            nodes_colors.append('green')

    return create_figure(nodes_colors)

# Callback para cambiar el texto del botón 'Cambiar tiempo'
@app.callback(
    Output('graph', 'figure', allow_duplicate=True),
    Input('change-time', 'n_clicks'),
    prevent_initial_call=True
)
def update_button_text(n_clicks):
    global colors_time, is_night

    if is_night:
        colors_time = ['white', 'black', '#e3e6ff']
        is_night = False
    else:
        colors_time = ['#2b2e47', 'white', '#4f5582']
        is_night = True
        
    return create_figure(['blue'] * len(G.nodes()))

# Callback al recargar la página se resetean valores 
@app.callback(
    Output('graph', 'figure', allow_duplicate=True),
    Input('url', 'pathname'),
    prevent_initial_call=True
)
def reload_page(pathname):
    global is_night, colors_time
    is_night = False
    colors_time = ['white', 'black', '#e3e6ff']
    return create_figure(['blue'] * len(G.nodes()))

# Correr la app
if __name__ == '__main__':
    app.run_server(debug=True)