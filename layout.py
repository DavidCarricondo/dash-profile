import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


card_content_1 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H5("Card with image", className="card-title"),
            html.P(
                "This card has an image on top, and a button below",
                className="card-text",
            ),
            html.A(html.Button("Let's go!"), href='https://www.github.com/DavidCarricondo'),
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