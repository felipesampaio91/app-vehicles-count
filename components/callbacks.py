from dash import Output, Input, State, dash_table
import plotly.express as px
import pandas as pd
from data.queries import get_vehicle_data
from utils.data_processing import process_vehicle_data
from utils.export_excel import export_to_excel

def register_callbacks(app):

    @app.callback(
        Output("vehicle-graph", "figure"),
        Output("data-table", "children"),
        Input("camera-dropdown", "value"),
        Input("date-picker-range", "start_date"),
        Input("date-picker-range", "end_date"),
        Input("time-start", "value"),
        Input("time-end", "value"),
    )
    def update_data(camera, start_date, end_date, time_start, time_end):
        empty_fig = {
            "data": [],
            "layout": {"title": "Sem dados para o período selecionado"}
            }
        if not camera or not start_date or not end_date:
            return empty_fig, ""

        start_dt = f"{start_date} {time_start}:00"
        end_dt = f"{end_date} {time_end}:59"


        raw_df = get_vehicle_data(camera, start_dt, end_dt)
        df = process_vehicle_data(raw_df)

        if df.empty:
            return empty_fig, ""

        fig = px.line(df, x="Data/Hora", y=["C1", "C2", "C3", "Total"], title="Contagem por Tipo de Veículo")

        table = dash_table.DataTable(
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("records"),
            page_size=10,
        )

        return fig, table

    @app.callback(
        Output("export-btn", "children"),
        Input("export-btn", "n_clicks"),
        State("camera-dropdown", "value"),
        State("date-picker-range", "start_date"),
        State("date-picker-range", "end_date"),
        State("time-start", "value"),
        State("time-end", "value"),
        prevent_initial_call=True
    )
    def export_data(n_clicks, camera, start_date, end_date, time_start, time_end):
        if not camera or not start_date or not end_date:
            return "Exportar XLSX"

        start_dt = f"{start_date} {time_start}"
        end_dt = f"{end_date} {time_end}"

        raw_df = get_vehicle_data(camera, start_dt, end_dt)
        df = process_vehicle_data(raw_df)

        if df.empty:
            return "Sem dados para exportar"

        export_to_excel(df, "relatorio.xlsx")
        return "Arquivo Exportado!"
