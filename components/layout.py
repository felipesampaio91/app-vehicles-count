from dash import dcc, html
import dash_bootstrap_components as dbc
from data.queries import get_camera_list

def generate_time_options():
    times = []
    for h in range(24):
        for m in (0, 15, 30, 45):
            times.append(f"{h:02d}:{m:02d}")
    return [{"label": t, "value": t} for t in times]

def create_layout():
    time_options = generate_time_options()
    camera_options = [{"label": cam, "value": cam} for cam in get_camera_list()]


    return dbc.Container([
        html.H1("Contagem Veicular", className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.Label("Câmera:"),
                dcc.Dropdown(
                    id="camera-dropdown",
                    options=camera_options,
                    placeholder="Selecione uma câmera"
                )
            ], width=3),

            dbc.Col([
                html.Label("Período:"),
                dcc.DatePickerRange(
                    id="date-picker-range",
                    display_format="YYYY-MM-DD",
                    start_date_placeholder_text="Data inicial",
                    end_date_placeholder_text="Data final"
                ),
                html.Br(), html.Br(),
                html.Label("Hora início:"),
                dcc.Dropdown(id='time-start', options=time_options, value='00:00'),
                html.Br(),
                html.Label("Hora fim:"),
                dcc.Dropdown(id='time-end', options=time_options, value='23:45'),
            ], width=6),

            dbc.Col([
                html.Br(),
                html.Button("Exportar XLSX", id="export-btn", n_clicks=0)
            ], width=3),
        ], className="mb-4"),

        dcc.Graph(id="vehicle-graph"),
        html.Hr(),
        html.Div(id="data-table")
    ], fluid=True)
