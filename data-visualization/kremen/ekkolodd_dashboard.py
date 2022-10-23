import pandas as pd
import plotly.express as px
import dash
from dash import dcc  # dash version 2.0.0
from dash import html  # dash version 2.0.0
import dash_bootstrap_components as dbc  # version 1.0.2

# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/
from dash.dependencies import Output, Input

app = dash.Dash(__name__)
#### READ THE DATA

df = pd.read_csv("../../data-processing/data/ekkolodd.csv")

all_data_graph = px.scatter(df, x="sample start time", y="distance", title="distance")
# Creating labels and values for dash components

start_time = [{"label": i, "value": i} for i in df[df.columns[0]].unique()]

## Dashboard
firstpage = [
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H3(
                        "Ocean Access Dashboard - Ekkolodd",
                        className="text-center mb-3 p-3",
                    ),
                    html.Hr(),
                ],
                width={"size": 12, "offset": 0, "order": 0},
            ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H6(
                        "Select the sample start time you want to look into:",
                        className="text-center mb-2 p-1",
                    ),
                    dcc.Dropdown(
                        id="start_time-dropdown",
                        options=start_time,
                        value=start_time[0]["label"],
                        clearable=False,
                    ),
                    # Display text information related to the selected buoy
                    html.Div(id="generalinfo", className="text-center p-2"),
                    html.Div(id="distancemean", className="text-center p-2"),
                    html.Div(id="confidencemean", className="text-center p-2"),
                ],
                width={"size": 4, "offset": 0, "order": 0},
            ),
            dbc.Col(
                [
                    html.H5("All ekkolodd data", className="text-center p-1"),
                    dcc.Graph(figure=all_data_graph, style={"height": 600}),
                ],
                width={"size": 8, "offset": 0, "order": 0},
            ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H5("Distance", className="text-center"),
                    html.H6(
                        "Ekkolodd distance data", className="text-center font-italic"
                    ),
                    dcc.Graph(id="distancechart", style={"height": 400}),
                ],
                width={"size": 6, "offset": 0, "order": 0},
            ),
            dbc.Col(
                [
                    html.H5("Confidence", className="text-center"),
                    html.H6(
                        "Ekkolodd confidence data",
                        className="text-center font-italic",
                    ),
                    dcc.Graph(id="confidencechart", style={"height": 400}),
                ],
                width={"size": 6, "offset": 0, "order": 0},
            ),
        ]
    ),
]

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(id="page-content", children=firstpage, className="p-3")


@callback(
    [
        # Output("allpressurechart", "figure"),
        Output("distancechart", "figure"),
        Output("confidencechart", "figure"),
        Output("generalinfo", "children"),
        Output("distancemean", "children"),
        Output("confidencemean", "children"),
    ],
    Input("start_time-dropdown", "value"),
)
def update_figure(start_time):

    df2 = df.loc[(df["sample start time"] == start_time)]
    df2 = df2.reset_index(drop=True)

    fig_distance = px.line(df2, y="distance", title="distance")
    fig_confidence = px.line(df2, y="confidence", title="confidence")

    # text info about current buoy
    generalinfo = f"Shows info for the ekkolodd sensor at start time {start_time}"
    distancemean = f"The mean of distance data values is: {df2['distance'].mean()}"
    confidencemean = (
        f"The mean of confidence data values is: {df2['confidence'].mean()}"
    )

    return (
        fig_distance,
        fig_confidence,
        generalinfo,
        distancemean,
        confidencemean,
    )


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
