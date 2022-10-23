import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash 
from dash import Output
from dash import dcc
from dash import html, Dash, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

""" 

app = Dash(__name__, use_pages=True)

app.config.suppress_callback_exceptions = True

# Import and clean data (importing csv into pandas)


# ------------------------------------------------------------------------------


# App layout

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

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

sidebar = html.Div(
    [
        html.H2("JOFEADAR", className="display-4"),
        html.Hr(),
        html.P(
            "Data processing, visualization and storing made simple!", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Visualization", href="/pages/kremen", active="exact"),
                dbc.NavLink("Files", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home()
    elif pathname == "/pages/kremen":
        return visualization()
    elif pathname == "/page-2":
        return files()
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


def home():
    return html.P("This is the content of the home page!"), 

def visualization():

    return kremen.layout
    

def files():
    return html.P("Here is the place you can download files")


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)


"""

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
            )
            for page in dash.page_registry.values()
        ],  
    ),
],   style=SIDEBAR_STYLE, )

content =  html.Div(dash.page_container, style=CONTENT_STYLE)

app.layout = html.Div([sidebar, content])

if __name__ == '__main__':
	app.run_server(debug=True)