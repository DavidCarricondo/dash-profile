import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from src.layout import *
from dash.dependencies import Input, Output, State
from src.app_dash import app, external_stylesheets, server

### Use lg, md, xs dbc.Col arguments to make it responsive to other screens like cellphones.
# check: https://medium.com/swlh/dashboards-in-python-for-beginners-using-dash-responsive-mobile-dashboards-with-bootstrap-css-2a0d05a53cf6
card = [
    dbc.Row([
        dbc.Col(),
        dbc.Col(text_card, lg=3, md=4, xs=12),
        dbc.Col()]),
    dbc.Row([
        dbc.Col(dbc.Card(card_content_1, color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(card_content_2, color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(card_content_3, color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(card_content_4, color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col(dbc.Card(card_content_5, color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(card_content_6, color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(card_content_7, color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
        dbc.Col(dbc.Card(card_content_8, color="dark", inverse=True, style={"width": "24rem", "height" : "29rem"}), lg=3, md=4, xs=12),
    ])
    ]

app.layout = html.Div(children=
                [   
                    html.Div(html.H1(dcc.Markdown("**Welcome to David Carricondo's profile**"), style={"text-align":"center", "background-color":'#000000'})),
                    html.Div(card),
                    html.Hr(),
                    html.Div(navbar)
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



