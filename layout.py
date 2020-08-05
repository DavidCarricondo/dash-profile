import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


card_content_1 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H5("Draw-me!", className="card-title"),
            html.P(
                "Desktop app that uses a custom CNN to classify drawings in a 'paint-like' interface. The app then substitute these drawings for the face features detected in a live web cam streaming via haar-cascades",
                className="card-text",
            ),
            html.A(html.Button("Let's take a look!"), href='https://www.github.com/DavidCarricondo/Draw-me'),
        ]
    ),
]

card_content_2 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H5("Book reviews analyzer", className="card-title"),
            html.P(
                "Dashboard written with Dash that uses Selenium to scrape the latest reviews of a book and analyzes their sentiment content using a custom recursive neural network",
                className="card-text",
            ),
            html.Hr(),
            html.A(html.Button("Let's take a look!"), href='https://github.com/DavidCarricondo/selenium-NLP'),
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