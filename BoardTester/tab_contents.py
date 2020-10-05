import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table

# ------------------------------------------------------------------------------
# Tab1 Contents
vs_params = ['vmax','vmin','ton']
dut_config_tab = dbc.Card(
    dbc.CardBody(
        [
            html.P("Configure the DUT", className="card-text"),
            dbc.Button("Save",
                        id="dut_config_button", 
                        color="primary"),
            # Voltage Source Table
            dash_table.DataTable(
                id='adding-rows-table',
                columns=(
                    [{'id': 'vs', 'name': 'Voltage Source'}] +
                    [{'id': p, 'name': p} for p in vs_params]
                ),
                data=[
                    dict(vs=i, **{param: 0 for param in vs_params})
                    for i in range(1, 2)
                ],
                editable=True,
                        row_deletable=True
                    ),
                    html.Button('Add Row', id='editing-rows-button', n_clicks=0),
        ]
    ),
    className="mt-3",
)
test_config_tab = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)
