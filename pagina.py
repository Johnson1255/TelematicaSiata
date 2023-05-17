from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sistema de Login"),
    html.Div(id="login-container", children=[
        html.Label("Usuario"),
        dcc.Input(id="input-username", type="text"),
        html.Label("Contraseña"),
        dcc.Input(id="input-password", type="password"),
        html.Button("Iniciar sesión", id="btn-login", n_clicks=0),
        html.Div(id="login-error", style={"color": "red", "margin-top": "10px"})
    ]),
    html.Div(id="graph-container", style={"display": "none"}, children=[
        html.H2("Niveles de Agua - SIATA"),
        dcc.Graph(id="siata-graph", style={'height': '600px'})
    ])
])

def validate_login(username, password):
    valid_username = "admin"
    valid_password = "password"
    return username == valid_username and password == valid_password

@app.callback(
    [Output("login-container", "style"),
     Output("graph-container", "style"),
     Output("login-error", "children"),
     Output("siata-graph", "figure")],
    [Input("btn-login", "n_clicks")],
    [State("input-username", "value"),
     State("input-password", "value")]
)
def login(n_clicks, username, password):
    if n_clicks > 0:
        if validate_login(username, password):
            url = "http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/?format=json"
            data = pd.read_json(url)
            df = pd.json_normalize(data['datos'])
            df['latitud'] = df['coordenadas'].apply(lambda x: x[0]['latitud'])
            df['longitud'] = df['coordenadas'].apply(lambda x: x[0]['longitud'])
            
            fig = px.scatter_mapbox(df, lat="latitud", lon="longitud", color="porcentajeNivel",
                                     color_continuous_scale="Viridis", size_max=15, zoom=10,
                                     mapbox_style="stamen-terrain")
            
            return {"display": "none"}, {"display": "block"}, "", fig
        else:
            return {}, {"display": "none"}, "Usuario o contraseña incorrectos", {}
    else:
        return {}, {"display": "none"}, "", {}

if __name__ == '__main__':
    app.run_server(debug=True)
