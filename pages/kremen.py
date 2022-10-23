import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import html, dcc, callback, Input, Output
import dash


dash.register_page(__name__)

#app = dash.Dash(__name__)

#### READ THE DATA


df = pd.read_csv("data-processing/data/ID123.csv")


## Figures

## Pressure vs depth fig


# fig_pressure_depth = px.scatter(df, x="depth", y="pressure", title="pressure vs. depth")
# fig_pressure_depth.update_layout(
#     title="pressure vs. depth", xaxis_title="kPa", yaxis_title="degrees C"
# )
# fig_pressure_depth.show()


## Pollution levels on all buoy ids

df.rename(columns={"oil_spill": "pollution"}, inplace=True)

# print(df.head())

# oil_spill default verdi 1
# dypde skal ha range

fig_all_pressure = px.scatter(
    data_frame=df,
    x="id",
    y="depth",
    animation_frame="time",
    animation_group="id",
    size="pollution",
    color="field",
    hover_name="id",
    facet_col="field",
    size_max=100,
    # category_orders={"Year": list(range(2007, 2019))},
    range_y=[0, 40],
    range_x=[0, 6],
)

# fig_all_pressure.show()


# Choose which robot you want to plot data for


# robot_id = 2
# field = "Frigg"
# df2 = df.loc[(df["id"] == robot_id) & (df["field"] == field)]


## Depth


# fig_depth = px.line(df2, x="time", y="depth", title="depth")
# fig_depth.update_layout(xaxis_title="time [h]", yaxis_title="depth [m]")
# fig_depth.show()


## Pressure


# fig_pressure = px.line(df2, x="time", y="pressure", title="pressure")
# fig_pressure.update_layout(xaxis_title="time [h]", yaxis_title="pressure [kPa]")
# fig_pressure.show()


## Temprature


# fig_temprature = px.line(df2, x="time", y="temperature", title="temperature")
# fig_temprature.update_layout(xaxis_title="time [h]", yaxis_title="temp [°C]")
# fig_temprature.show()


## Pollution


# fig_pollution = px.line(df2, x="time", y="pollution", title="pollution")
# fig_pollution.update_layout(xaxis_title="time [h]", yaxis_title="pollution [ppm]")
# fig_pollution.show()


from dash import dcc  # dash version 2.0.0
from dash import html  # dash version 2.0.0
import dash_bootstrap_components as dbc  # version 1.0.2

# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/
from dash.dependencies import Output, Input


# Creating labels and values for dash components


fields = [{"label": i, "value": i} for i in df[df.columns[1]].unique()]
ids = [{"label": i, "value": i} for i in df[df.columns[2]].unique()]

## Reference only
firstpage = [
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H3("Ocean Access Dashboard", className="text-center mb-3 p-3"),
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
                        "Select the field  you want to look into:",
                        className="text-center mb-2 p-1",
                    ),
                    dcc.Dropdown(
                        id="field-dropdown",
                        options=fields,
                        value=fields[0]["label"],
                        clearable=False,
                    ),
                    html.H6(
                        "Select the buoy you want to look into:",
                        className="text-center mb-2 p-1",
                    ),
                    dcc.Dropdown(
                        id="id-dropdown",
                        options=ids,
                        value=ids[0]["label"],
                        clearable=False,
                    ),
                    # Display text information related to the selected buoy
                    html.Div(id="generalinfo", className="text-center p-2"),
                    html.Div(id="depthmean", className="text-center p-2"),
                    html.Div(id="pressuremean", className="text-center p-2"),
                    html.Div(id="temperaturemean", className="text-center p-2"),
                    html.Div(id="pollutionmean", className="text-center p-2"),
                    html.Div(id="depthmax", className="text-center p-2"),
                    html.Div(id="pressuremax", className="text-center p-2"),
                    html.Div(id="pollutionmax", className="text-center p-2"),
                ],
                width={"size": 4, "offset": 0, "order": 0},
            ),
            dbc.Col(
                [
                    html.H5(
                        "Pollution levels on all buoy ids", className="text-center p-1"
                    ),
                    dcc.Graph(figure=fig_all_pressure, style={"height": 600}),
                ],
                width={"size": 8, "offset": 0, "order": 0},
            ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H5("Depth", className="text-center"),
                    html.H6(
                        "How deep is your love", className="text-center font-italic"
                    ),
                    dcc.Graph(id="depthchart", style={"height": 400}),
                ],
                width={"size": 3, "offset": 0, "order": 0},
            ),
            dbc.Col(
                [
                    html.H5("Pressure", className="text-center"),
                    html.H6(
                        "How much pressure on the device",
                        className="text-center font-italic",
                    ),
                    dcc.Graph(id="pressurechart", style={"height": 400}),
                ],
                width={"size": 3, "offset": 0, "order": 0},
            ),
            dbc.Col(
                [
                    html.H5("Temprature", className="text-center"),
                    html.H6(
                        "How hot is the water", className="text-center font-italic"
                    ),
                    dcc.Graph(id="tempraturechart", style={"height": 400}),
                ],
                width={"size": 3, "offset": 0, "order": 0},
            ),
            dbc.Col(
                [
                    html.H5("Pollution", className="text-center"),
                    html.H6(
                        "Oil spill in the area", className="text-center font-italic"
                    ),
                    dcc.Graph(id="pollutionchart", style={"height": 400}),
                ],
                width={"size": 3, "offset": 0, "order": 0},
            ),
        ]
    ),
]

#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = html.Div(id="page-content", children=firstpage, className="p-3")


@callback(
    [
        # Output("allpressurechart", "figure"),
        Output("depthchart", "figure"),
        Output("pressurechart", "figure"),
        Output("tempraturechart", "figure"),
        Output("pollutionchart", "figure"),
        Output("generalinfo", "children"),
        Output("depthmean", "children"),
        Output("pressuremean", "children"),
        Output("temperaturemean", "children"),
        Output("pollutionmean", "children"),
        Output("depthmax", "children"),
        Output("pressuremax", "children"),
        Output("pollutionmax", "children"),
    ],
    Input("field-dropdown", "value"),
    Input("id-dropdown", "value"),
)
def update_figure(field, robot_id):

    df2 = df.loc[(df["id"] == robot_id) & (df["field"] == field)]

    fig_depth = px.line(df2, x="time", y="depth", title="depth")
    fig_pressure = px.line(df2, x="time", y="pressure", title="pressure")
    fig_temprature = px.line(df2, x="time", y="temperature", title="temperature")
    fig_pollution = px.line(df2, x="time", y="pollution", title="pollution")

    # text info about current buoy
    generalinfo = (
        f"Shows info for the pollution sensor buoy {robot_id} at oil-field {field}"
    )
    depthmean = f"The mean of depth data values is: {df2['depth'].mean()}"
    pressuremean = f"The mean of pressure data values is: {df2['pressure'].mean()}"
    temperaturemean = (
        f"The mean of temperatures data values is: {df2['temperature'].mean()}"
    )
    pollutionmean = f"The mean of pollution data values is: {df2['pollution'].mean()}"
    depthmax = f"The maximum depth the buoy registered was: {df2['depth'].max()}"
    pressuremax = (
        f"The maximum pressure the buoy registered was: {df2['pressure'].max()}"
    )
    pollutionmax = (
        f"The maximum pollution registered by the buoy was: {df2['pollution'].max()}"
    )

    return (
        fig_depth,
        fig_pressure,
        fig_temprature,
        fig_pollution,
        generalinfo,
        depthmean,
        pressuremean,
        temperaturemean,
        pollutionmean,
        depthmax,
        pressuremax,
        pollutionmax,
    )

