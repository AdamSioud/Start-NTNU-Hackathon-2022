import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash 
from dash import Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Import and clean data (importing csv into pandas)

df = pd.read_csv("../data-processing/data/ekkolodd.csv")
print(df[:10])

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
                dbc.NavLink("Visualization", href="/page-1", active="exact"),
                dbc.NavLink("Files", href="/page-2", active="exact"),
                dbc.NavLink("About", href="/page-3", active="exact"),
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
    elif pathname == "/page-1":
        return visualization()
    elif pathname == "/page-2":
        return files()
    elif pathname == "/page-3":
        return about()
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
    return html.P("This is the content of the home page!")

def visualization():

    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

    fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

    tekst = html.Div([ html.P("This is the content of page visualization. Yay!"), html.Br(),
    dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown'), html.Div(id='dd-output-container') , dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
    ])

    @app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
    )

            
    def update_output(value):
        return f'You have selected {value}'

    return tekst
    

def files():
    return html.P("This is the content of files Yay! Get raw data files: Get clean data files, Generate files")

def about():
    return html.P("Oh cool, this is our about page")


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components




# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)