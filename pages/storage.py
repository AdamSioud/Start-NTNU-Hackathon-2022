# This file only let's you download files generated by "any" function, future needs to be connected to data-storage, GCP.

from doctest import ELLIPSIS_MARKER
import dash
from dash.dependencies import Output, Input 
from dash import dcc, html, callback
import datetime 



dash.register_page(__name__)


layout = html.Div([
    html.H2("Your file storage system", className="display-4"),
        html.Hr(),
        html.P(
            "On this page you have possibility to download all the data you have checked out on the dashboard, fully, and also raw files.", className="lead"
        ),
    html.Button("Download first raw file", id="btn_txt"), dcc.Download(id="download-text-index")]
)



@callback(Output("download-text-index", "data"), Input("btn_txt", "n_clicks"))
def func(n_clicks):

    time_now = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S') 

    newDict = {}
    with open('data-processing/raw/ekkolodd.txt', 'r') as f:
        for line in f:
            try:
                    
                splitLine = line.split()
                newDict[str(splitLine[0])] = ",".join(splitLine[1:])
            except ValueError:
                pass

    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    else:        
        return dict(content=str(newDict), filename=time_now)


#  To Do's in storage
#  Dynamically change file from user input, from what user wants he get then download files
#  These files could be stored locally in the first place, but should in end product be first stored in GCP then downloaded from user.
#  Then a user can always download files which have been generated in the past