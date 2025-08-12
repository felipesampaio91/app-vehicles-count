from dash import Dash
from components.layout import create_layout
from components.callbacks import register_callbacks
from config.settings import DASH_HOST, DASH_PORT, DEBUG

app = Dash(__name__)
app.title = "Contagem de Veiculos"

app.layout = create_layout()

register_callbacks(app)
if __name__ == "__main__":
    app.run_server(host=DASH_HOST, port=DASH_PORT, debug=DEBUG)