# Cody Holthus - Rip City Robotics

# Example APP structure
'''Top_folder
    |_index.py
    |_Assets
    |_Layouts
            |_Tab1.py
            |_Tab2.py
    |_Database
        |_board_name_test_name_datetime.xlsx (or .csv)
'''

# Configure_Dut_Tab.py ################################
#   - Contains the following prompts
#       1) Enter Number of Voltage Inputs
#           - Use input to create DataFrame and 
#           - display editabletable delow
#
#       2) Enter Number of Current Inputs
#           - Use input to create DataFrame and 
#           - display editabletable delow
#
#       3) Enter Number of Temperatures
#           - Use input to create DataFrame and 
#           - display editabletable delow
#
#       4) Enter Number of Digital Inputs
#           - Use input to create DataFrame and 
#           - display editabletable delow
#
#       5) Enter Number of Digital Outputs
#           - Use input to create DataFrame and 
#           - display editabletable delow

# Tab1.py ##################################### 
# 

### TABS
### Configure DUT
### - details above
### - dropdown to select lab device (labjack, SAILY, Digilent)
### Cofigure Test
### Simulation (Expected Results)
### Start Test (Live Updates)

import time

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

from tab_contents import vs_params, dut_config_tab, test_config_tab


#tc = TabContents()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


# ------------------------------------------------------------------------------
# App layout

app.layout = dbc.Container(
    [
        dcc.Store(id="store"),
        html.H1("PCB Design Verification Testing App"),
        html.H6("PCB P/N:   {pcb_pn}, PCB Name:   {pcb_name}, Test Date:   {date}"),
        html.Hr(),
        dbc.Tabs(
            [
                dbc.Tab(label="1 - Configure DUT", 
                        tab_id="dut_config_tab"),

                dbc.Tab(label="2 - Configure Test", 
                        tab_id="test_config_tab"),

                dbc.Tab(label="3 - Simulate", 
                        tab_id="simulate_tab"),

                dbc.Tab(label="4 - Run Test", 
                        tab_id="run_test_tab"),
            ],
            id="tabs"
        )
,
        html.Div(id="tab-content", className="p-4"),
    ]
)

#  Switching Tabs
@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")],
)
def switch_tab(active_tab, data):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    if active_tab == 'dut_config_tab' and data is None:
            return dut_config_tab
    else:
        return "No tab selected"

@app.callback(
    Output('adding-rows-table', 'data'),
    [Input('editing-rows-button', 'n_clicks')],
    [State('adding-rows-table', 'data'),
     State('adding-rows-table', 'columns')])
def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows

# Use Client side callbacks for data storage.


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
    #app.run_server(dev_tools_hot_reload=False)
    #app.run_server(mode='inline')

