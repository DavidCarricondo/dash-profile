import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from src.layout import *
from src.project_dictionary import project_dictionary
from dash.dependencies import Input, Output, State
from src.app_dash import app, external_stylesheets, server

### Use lg, md, xs dbc.Col arguments to make it responsive to other screens like cellphones.
# check: https://medium.com/swlh/dashboards-in-python-for-beginners-using-dash-responsive-mobile-dashboards-with-bootstrap-css-2a0d05a53cf6
card = [
    dbc.Row([
        dbc.Col(text_card, lg=4, md=5, xs=12),
    ],justify='center'),
    dbc.Row([
        dbc.Col(dbc.Card(generate_card(1, project_dictionary), color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(generate_card(2, project_dictionary, spaces=1), color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(generate_card(3, project_dictionary), color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(generate_card(4, project_dictionary, spaces=1), color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col(dbc.Card(generate_card(5, project_dictionary), color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(generate_card(6, project_dictionary, spaces=1), color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(generate_card(7, project_dictionary, spaces=1), color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(generate_card(8, project_dictionary, spaces=4), color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
    ])
    ]

app.layout = html.Div(children=
                [   
                    html.Div(html.H1(dcc.Markdown("**Welcome to David Carricondo's profile**"), style={"text-align":"center", "background-color":'#000000'})),
                    html.Div(card),
                    html.Hr(),
                    dbc.Row(dbc.Col(html.Div(navbar), lg=12, md=12, xs=12))
                ]
            )

app.title = "David Carricondo's data projects"

#Callbacks

for i in range(1,9):

    @app.callback(
        Output("popover"+str(i), "is_open"),
        [Input("popover-target"+str(i), "n_clicks")],
        [State("popover"+str(i), "is_open")],
    )
    def toggle_popover(n, is_open):
        if n:
            return not is_open
        return is_open


if __name__ == '__main__':
    app.run_server(debug=True)



