import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

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


cards = dbc.CardColumns(
    [
        dbc.Card(card_content_1, color="primary", inverse=True),
        dbc.Card(card_content_1, color="primary", inverse=True),
        dbc.Card(card_content_1, color="primary", inverse=True),
        dbc.Card(card_content_1, color="primary", inverse=True)
    ]
)



app.layout = html.Div(children=
    [
        html.H1('My data projects'),
        cards,
    ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)



