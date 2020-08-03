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


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavLink('My Linkedin', href='https://www.linkedin.com/in/david-carricondo-sanchez/', className='lead'),
        dbc.NavLink('My Github', href='https://github.com/DavidCarricondo', className='lead'),
            
    ],
    brand="You can know more about me here: ",
    brand_href="#",
    color="dark",
    dark=True,
)


#footer = html.Footer([html.A(html.Img(src="linkedin_image.png", style={'height':'50%', 'width':'50%', 'text-align':'right'}), href='https://www.linkedin.com/in/david-carricondo-sanchez/'),
#                    html.A(html.Img(src='github_image.png' ,style={'height':'50%', 'width':'50%', 'text-align':'right'}), href='https://github.com/DavidCarricondo')])

card = [
    dbc.Row([
        dbc.Col(dbc.Card(card_content_1, color="primary", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="success", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="danger", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="warning", inverse=True, style={"width": "24rem"})),
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col(dbc.Card(card_content_1, color="info", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="light", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="dark", inverse=True, style={"width": "24rem"})),
        dbc.Col(dbc.Card(card_content_1, color="primary", inverse=True, style={"width": "24rem"})),
    ])
    ]

app.layout = html.Div(children=
                [   
                    html.Div(html.H1("Welcome to David Carricondo's profile"), style={'color':'dark'}),
                    html.Div(navbar),
                    html.Div(card)
                ]
            )

app.title = "David Carricondo's profile"


if __name__ == '__main__':
    app.run_server(debug=True)



