import os
from dash import Dash
from components.layout import create_layout
from components.callbacks import register_callbacks
from config.settings import DASH_HOST, DASH_PORT, DEBUG

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

DASH_HOST = os.getenv("DASH_HOST", "0.0.0.0")
DASH_PORT = int(os.getenv("DASH_PORT", 8055))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

app = Dash(__name__)
app.title = "Contagem de Veiculos"

app.layout = create_layout()

register_callbacks(app)
if __name__ == "__main__":
    app.run(host=DASH_HOST, port=DASH_PORT, debug=DEBUG)