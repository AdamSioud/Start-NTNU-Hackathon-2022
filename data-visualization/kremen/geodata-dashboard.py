import pandas as pd
import plotly.express as px
import dash
from dash import dcc  # dash version 2.0.0
from dash import html  # dash version 2.0.0
import dash_bootstrap_components as dbc  # version 1.0.2
import plotly.graph_objects as go

# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/
from dash.dependencies import Output, Input

app = dash.Dash(__name__)
#### READ THE DATA

NUM_BUOYS = [5, 3, 7, 5, 4, 4]
geo_data = pd.read_csv("data-processing/data/geo_data.csv")
OIL_FIELDS = geo_data["field"].unique()
COLORS = [
    px.colors.sequential.Teal,
    px.colors.sequential.Purples,
    px.colors.sequential.Greens,
    px.colors.sequential.Reds,
    px.colors.sequential.Blues,
    px.colors.sequential.Electric,
]

fig = go.Figure(go.Scattermapbox())

field_plots = []
for idx, field in enumerate(OIL_FIELDS):
    field_df = geo_data[geo_data["field"] == field]
    for i in range(NUM_BUOYS[idx]):
        id_field_df = field_df[field_df["id"] == i]
        fig.add_trace(
            go.Scattermapbox(
                name=f"{id_field_df['field'].iloc[0]} {id_field_df['id'].iloc[0]}",
                mode="markers+lines",
                lat=id_field_df["lat"],
                lon=id_field_df["lon"],
                marker={"size": 5},
                line=dict(color=COLORS[idx][i]),
            )
        )
fig.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    mapbox={
        "style": "stamen-terrain",
        "zoom": 6,
        "center": {"lon": 2, "lat": 59},
    },
)
# Creating labels and values for dash components

## Dashboard
firstpage = [
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H3(
                        "Ocean Access Dashboard - Map",
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
                    dcc.Graph(figure=fig, style={"height": "85vh"}),
                ],
                width={"size": 12, "offset": 0, "order": 0},
                # className="mb-10",
            ),
        ],
    ),
]

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(id="page-content", children=firstpage, className="p-3")


# @app.callback(
#     [
#         # Output("allpressurechart", "figure"),
#         Output("distancechart", "figure"),
#         Output("confidencechart", "figure"),
#         Output("generalinfo", "children"),
#         Output("distancemean", "children"),
#         Output("confidencemean", "children"),
#     ]
# )
# def update_figure(start_time):

#     df2 = df.loc[(df["sample start time"] == start_time)]
#     df2 = df2.reset_index(drop=True)

#     fig_distance = px.line(df2, y="distance", title="distance")
#     fig_confidence = px.line(df2, y="confidence", title="confidence")

#     # text info about current buoy
#     generalinfo = f"Shows info for the ekkolodd sensor at start time {start_time}"
#     distancemean = f"The mean of distance data values is: {df2['distance'].mean()}"
#     confidencemean = (
#         f"The mean of confidence data values is: {df2['confidence'].mean()}"
#     )

#     return (
#         fig_distance,
#         fig_confidence,
#         generalinfo,
#         distancemean,
#         confidencemean,
#     )


if __name__ == "__main__":
    app.run_server(debug=True, port=8052)
