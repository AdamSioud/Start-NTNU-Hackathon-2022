import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash 
from dash import Output
from dash import dcc
from dash import html, Dash, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout

# the style arguments for the sidebar. We use position:fixed and a fixed width

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}




sidebar = html.Div([
	html.H2("JOFEADAR", className="display-4"),
        html.Hr(),
        html.P(
            "Data processing, visualization and storing made simple!", className="lead"
        ),

    html.Div(
        [
            dcc.Link(
                f"{page['name']}", href=page["relative_path"]
            , className="row p-3")
            for page in dash.page_registry.values()
        ],  
    ),
],   style=SIDEBAR_STYLE, )

content =  html.Div(dash.page_container, style=CONTENT_STYLE)

app.layout = html.Div([sidebar, content])

if __name__ == '__main__':
	app.run_server(debug=True)