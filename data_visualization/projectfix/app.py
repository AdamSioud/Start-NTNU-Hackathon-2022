import pandas as pd
import dash # I am using version 2.0.0
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.graph_objects as go


# Import and clean data (importing csv into pandas)

df = pd.read_csv("../../data-processing/data/ekkolodd.csv")
print(df[:10])


# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

"""
fig_main = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])]) 

"""
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]


"""
app.layout = dbc.Container(
    [
        # First and only row
        dbc.Row([
            # First column
            dbc.Col([
                # CHART
            ], width = {}),
            # Second column
            dbc.Col([
                # dropdown
            ], width = {}),            
        ])
    ]
)

ticker_dict = [
    {'label': 'Apple, Inc.', 'value': 'AAPL'},
    {'label': 'Advanced Micro Devices, Inc.', 'value': 'AMD'},
    {'label': 'Facebook, Inc.', 'value': 'FB'},
    {'label': 'Riot Blockchain, Inc.', 'value': 'RIOT'},
    {'label': 'Sunrun Inc.', 'value': 'RUN'},
    {'label': 'Tesla, Inc.', 'value': 'TSLA'}
]


app.layout = dbc.Container(
    [
        # First and only row
        dbc.Row([
            # First column
            dbc.Col([
                html.Hr(),
                html.H5('Price chart', className='text-center'),
                dcc.Graph(id='chart',
                          figure=fig_main,
                          style={'height':750},
                          ),
            ],
                width={'size': 9, 'offset': 0, 'order': 2}),
            # Second column
            dbc.Col([
                html.Hr(),
                html.H5('Select the stock', className='text-center'),
                html.Hr(),
                dcc.Dropdown(
                    id='ticker-selector',
                    options=ticker_dict,
                    value='AMD',
                    clearable=False,
                ),
            ],
                width={'size': 3, 'offset': 0, 'order': 1}),
        ]),
        
    ], fluid=True)

@app.callback(
    [Output("chart", "figure"), Output("div-input", "children")],
    [Input("ticker-selector", "value")]
)


def render_tickerchart(value):
    t_candles = pd.read_csv('prices/{}_price_hist.csv'.format(value))
    fig_main = go.Figure()
    fig_main.add_trace(go.Candlestick(x=t_candles["date"],
                                      open=t_candles["open"],
                                      high=t_candles["high"],
                                      low=t_candles['low'],
                                      close=t_candles['close'],
                                      name="OHLC",
                                      showlegend=False))

    fig_main.update(layout_xaxis_rangeslider_visible=False)
    fig_main.update_layout(margin = dict(t=50, b=50, l=25, r=25))
    return fig_main, value

"""



""" 
d = pd.DataFrame(df)
dd_labels = [{'label': d[0].unique()[i], 'value': d[0].unique()[i]} for i in range(d[0].unique().shape[0])]
dd_labels

"""

## Reference only
firstpage_ = [
    dbc.Row([
        dbc.Col([
            
        ],
            width={'size': 12, 'offset': 0, 'order': 0}),
    ]),
    dbc.Row([
        dbc.Col([
            
        ],
            width={'size': 4, 'offset': 0, 'order': 0}),

        dbc.Col([
            
        ],
            width={'size': 8, 'offset': 0, 'order': 0}),
    ]),
    dbc.Row([
        dbc.Col([
            
        ],
            width={'size': 4, 'offset': 0, 'order': 0}),
        dbc.Col([
            
        ],
            width={'size': 4, 'offset': 0, 'order': 0}),
        dbc.Col([
            
        ],
            width={'size': 4, 'offset': 0, 'order': 0}),
    ]),
]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "JOFEADAR"



app.layout = html.Div(id='page-content', children=firstpage, className='p-3')


if __name__ == "__main__":
    app.run_server(debug=True)
