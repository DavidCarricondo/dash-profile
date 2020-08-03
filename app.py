import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = [dbc.themes.DARKLY]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

card_content_1 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H5("Card with image", className="card-title"),
            html.P(
                "This card has an image on top, and a button below",
                className="card-text",
            ),
            dbc.Button("Click me!", color="primary"),
        ]
    ),
]


navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    html.Div(id="banner-text",children=[
                                                        html.H2("David Carricondo Sánchez"),
                                                        html.H3("My Profile"),
                                                        ])
                ],
                align="center",
                no_gutters=False,
            ),
        ),
        dbc.Nav(dbc.Row([
                    dbc.Col(dbc.NavLink('My Linkedin', href='https://www.linkedin.com/in/david-carricondo-sanchez/')),
                    dbc.Col(dbc.NavLink('My Github', href='https://github.com/DavidCarricondo')),
        ]))
    ],
    color="dark",
    dark=True
    )

'''
navbar=html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H2("David Carricondo Sánchez"),
                    html.H3("My Profile"),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.Button(
                        id="learn-more-button", children="LEARN MORE", n_clicks=0
                    ),
                    html.Img(id="logo", src=app.get_asset_url("dash-logo-new.png")),
                ],
            ),
        ],
    )
'''
card = [
    dbc.Row([
        dbc.Col(dbc.Card(card_content_1, color="primary", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="primary", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="primary", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="primary", inverse=True, style={"width": "24rem"})),
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col(dbc.Card(card_content_1, color="primary", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="primary", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="primary", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="primary", inverse=True, style={"width": "24rem"})),
    ])
    ]

app.layout = html.Div(children=
                [   
                    html.Div(navbar),
                    html.Div(card)
                ]
            )

if __name__ == '__main__':
    app.run_server(debug=True)



