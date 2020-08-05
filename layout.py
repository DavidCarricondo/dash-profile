import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


card_content_1 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H4(dcc.Markdown("**Draw-me!**"), className="card-title"),
            html.P(
                "Desktop app that uses a custom CNN to classify drawings in a 'paint-like' interface. The app then substitute these drawings for the face features detected in a live web cam streaming via haar-cascades.",
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
            html.H4(dcc.Markdown("**Book reviews analyzer**"), className="card-title"),
            html.P(
                "Dashboard written with Dash that uses Selenium to scrape the latest reviews of a book and analyzes their sentiment content using a custom recursive neural network.",
                className="card-text",
            ),
            html.Hr(),
            html.A(html.Button("Let's take a look!"), href='https://github.com/DavidCarricondo/selenium-NLP'),
        ]
    ),
]

card_content_3 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H4(dcc.Markdown("**API-chat-recommender!**"), className="card-title"),
            html.P(
                "This is an API for data extraction, user recommendation, and sentiment analysis of a chat. The API is deployed as a docker container in a Heroku server using a MongoDB Atlas database in the cloud.",
                className="card-text",
            ),
            html.A(html.Button("Let's take a look!"), href='https://github.com/DavidCarricondo/SW_chat-Sentiment-recommender'),
        ]
    ),
]

card_content_4 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H5(dcc.Markdown("**Goodreads reviews custom database**"), className="card-title"),
            html.P(
                "I used Selenium to automate the scrapping of the latest 60 reviews posted in the website of more than 1000 titles. The clean version contains a total of 22512 reviews. The main usage is sentiment prediction.",
                className="card-text",
            ),
            html.A(html.Button("Let's take a look!"), href='https://github.com/DavidCarricondo/Custom-database-goodreads-reviews'),
        ]
    ),
]


card_content_5 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H4(dcc.Markdown("**Pipeline-project: Dancing to your band**"), className="card-title"),
            html.P(
                "Data pipelines that uses a kaggle data set enriched with data from two different APIS (with and without APIKEY) and from wikipedia scrapping that generate a report on a given music band.",
                className="card-text",
            ),
            html.A(html.Button("Let's take a look!"), href='https://github.com/DavidCarricondo/data-analysis-pipeline'),
        ]
    ),
]

card_content_6 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H4(dcc.Markdown("**Diamond prices prediction with ML**"), className="card-title"),
            html.P(
                "Data exploration, cleaning and modelling of a diamonds dataset. I use sklearn and h20 as machine learning frameworks",
                className="card-text",
            ),
            html.Hr(),
            html.A(html.Button("Let's take a look!"), href='https://github.com/DavidCarricondo/Diamond-prices-ML-Kaggle-competition'),
        ]
    ),
]

card_content_7 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H4(dcc.Markdown("**Choosing best location for company**"), className="card-title"),
            html.P(
                "In this project I make extensive use of mongo queries on unstructure data extracted from different APIs.",
                className="card-text",
            ),
            html.Hr(),
            html.A(html.Button("Let's take a look!"), href='https://github.com/DavidCarricondo/mongo-project'),
        ]
    ),
]

card_content_8 = [
    dbc.CardImg(src="https://media.giphy.com/media/9DavVitIZ26jH0aK7s/giphy.gif", top=True),
    dbc.CardBody(
        [
            html.H4(dcc.Markdown("**My profile dashboard**"), className="card-title"),
            html.P(
                "I created a dashboard with dash as a profile of my most relevant data projects.",
                className="card-text",
            ),
            html.Hr(),
            html.Hr(),
            html.Hr(),
            html.Hr(),
            html.A(html.Button("Let's take a look!"), href='https://github.com/DavidCarricondo/Custom-database-goodreads-reviews'),
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

text_card = html.Div([html.H4('Take a look at my data science projects', className='card-header', style={'color': 'primary', 'text-align': 'center'}), 
    html.Div('Thanks for visiting my profile! These are some quick descriptions of the most relevant data project I have been working on. Click on the button in each card to be redirected to the github page \
        of each of the projects. If you want to know more about me, click on the links in the footer. Enjoy your stay!', className='card-text')], className="card border-success mb-3")
        