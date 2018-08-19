"""
REFERENCE: The official dash documentation: https://dash.plot.ly/live-updates was used to code some of this
scripts sections. 
"""
#Import required modules
import dash
import dash_html_components as html
from flask import Flask
import sqlite3 
import dash_core_components as dcc
from dash.dependencies import Event, Output
import plotly

#initialises database to sensehat database
dbname = '/home/pi/Assignment_1/sensehat.db'
#initialises server to Flask object
server = Flask(__name__)
#initialises application to a Dash object and parses in the Flask server
app = dash.Dash(__name__, server=server, url_base_pathname='/pigraph/')
#Set up for Dash html page layout
app.layout = html.Div(children=[
    html.H1(children='Raspberry Pi Temperature and Humidity Data'),

    dcc.Graph(id='live-graph', animate=True),
    dcc.Interval(
        id='graph-update',
        interval=1*1000
    )
])
#Method for updating the graph using the sensehat databse data
@app.callback(Output('live-graph', 'figure'), events=[Event('graph-update', 'interval')])
def update_graph():
    data = {
        'datetime':[],
        'temp': [], 
        'humidity': []
    }
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for row in curs.execute("SELECT * FROM SENSEHAT_data"):
        data['datetime'].append(str(row[0]))
        data['temp'].append(row[1])
        data['humidity'].append(row[2])

    temp_trace = plotly.graph_objs.Scatter(
        x=data['datetime'],
        y=data['temp'],
        name='Temperature',
        mode='lines+markers',
    )

    humid_trace = plotly.graph_objs.Scatter(
        x=data['datetime'],
        y=data['humidity'],
        name='Humidity',
        mode='lines+markers',
    )

    graph_data = [temp_trace, humid_trace]
    layout = plotly.graph_objs.Layout()

    return {'data':graph_data,'layout':layout}

#Main website route
@server.route('/')
def index():
    return """ <h1>Welcome</h1> """
#Excutes the script on public host, port 5000
if __name__ == '__main__':
    server.run(host= '0.0.0.0', port= 5000, debug=True)