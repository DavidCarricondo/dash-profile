import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from src.app_dash import app

def generate_card(project_number, project_dictionary):
    proj = project_dictionary[str(project_number)]
    card_content = [
        dbc.CardImg(src=app.get_asset_url(proj['image']), top=True, style={'height':'14rem'}),
        dbc.CardBody(
            [
                html.H4(dcc.Markdown(proj['title']), className="card-title"),
                html.P(proj['desc'], className="card-text",),
                dbc.Row([
                    dbc.Col(html.A(html.Button("Take a look!", style={'color':'dark', 'hight':'1.5rem'}), href=proj['link']),),
                    dbc.Col([
                        dbc.Button('Technologies', id='popover-target'+str(project_number), style={'color':'primary', 'height':'2rem', 'vertical-align':'top'}),
                        dbc.Popover([
                            dbc.PopoverBody(dcc.Markdown(proj['technologies']))
                        ],id='popover'+str(project_number), is_open=False, target='popover-target'+str(project_number))
                    ])
                ])
            ]
        ),
    ]
    return card_content

# card_content_1 = [
#     dbc.CardImg(src=app.get_asset_url('drawme.png'), top=True, style={'height':'14rem'}),
#     dbc.CardBody(
#         [
#             html.H4(dcc.Markdown("**Draw-me!**"), className="card-title"),
#             html.P(
#                 "Desktop app that uses a custom CNN to classify drawings in a 'paint-like' interface. The app then substitute these drawings for the face features detected in a live web cam streaming via haar-cascades.",
#                 className="card-text",
#             ),
#             dbc.Row([
#                 dbc.Col(html.A(html.Button("Take a look!", style={'color':'dark', 'hight':'1.5rem'}), href='https://www.github.com/DavidCarricondo/Draw-me'),),
#                 dbc.Col([
#                     dbc.Button('Technologies', id='popover-target1', style={'color':'primary', 'height':'2rem', 'vertical-align':'top'}),
#                     dbc.Popover([
#                         dbc.PopoverBody(dcc.Markdown(
#                             '''
#                             + Tensorflow 
#                             + Keras 
#                             + OpenCv
#                             + Tkinter
#                             + Neural networks
#                             + Haar cascades
#                             '''))
#                     ],id='popover1', is_open=False, target='popover-target1')
#                 ])
#             ])
#         ]
#     ),
# ]

# card_content_2 = [
#     dbc.CardImg(src=app.get_asset_url('Dashboard_demo.gif'), top=True, style={'height':'14rem'}),
#     dbc.CardBody(
#         [
#             html.H4(dcc.Markdown("**Book reviews analyzer**"), className="card-title"),
#             html.P(
#                 "Dashboard written with Dash that uses Selenium to scrape the latest reviews of a book and analyzes their sentiment content using a custom recursive neural network.",
#                 className="card-text",
#             ),
#             html.Hr(),
#             dbc.Row([
#                 dbc.Col(html.A(html.Button("Take a look!", style={'color':'dark', 'hight':'1.5rem'}), href='https://github.com/DavidCarricondo/selenium-NLP'),),
#                 dbc.Col([
#                     dbc.Button('Technologies', id='popover-target2', style={'color':'primary', 'height':'2rem', 'vertical-align':'top'}),
#                     dbc.Popover([
#                         dbc.PopoverBody(dcc.Markdown(
#                             '''
#                             + Dash 
#                             + Selenium 
#                             + Tensorflow
#                             + NLP
#                             + Neural networks
#                             + Plotly
#                             '''))
#                     ],id='popover2', is_open=False, target='popover-target2')
#                 ])
#             ])
#         ]
#     ),
# ]

# card_content_3 = [
#     dbc.CardImg(src=app.get_asset_url('recommender_gif.gif'), top=True, style={'height':'14rem'}),
#     dbc.CardBody(
#         [
#             html.H4(dcc.Markdown("**API-chat-recommender!**"), className="card-title"),
#             html.P(
#                 "This is an API for data extraction, user recommendation, and sentiment analysis of a chat. The API is deployed as a docker container in a Heroku server using a MongoDB Atlas database in the cloud.",
#                 className="card-text",
#             ),
#             dbc.Row([
#                 dbc.Col(html.A(html.Button("Take a look!", style={'color':'dark', 'hight':'1.5rem'}), href='https://github.com/DavidCarricondo/SW_chat-Sentiment-recommender'),),
#                 dbc.Col([
#                     dbc.Button('Technologies', id='popover-target3', style={'color':'primary', 'height':'2rem', 'vertical-align':'top'}),
#                     dbc.Popover([
#                         dbc.PopoverBody(dcc.Markdown(
#                             '''
#                             + Flask 
#                             + Beautiful soup 
#                             + nltk
#                             + Docker
#                             + Mongo Atlas
#                             + Heroku
#                             '''))
#                     ],id='popover3', is_open=False, target='popover-target3')
#                 ])
#             ])
#         ]
#     ),
# ]

# card_content_4 = [
#     dbc.CardImg(src=app.get_asset_url('gr_database_image.png'), top=True, style={'height':'14rem'}),
#     dbc.CardBody(
#         [
#             html.H5(dcc.Markdown("**Goodreads reviews custom database**"), className="card-title"),
#             html.P(
#                 "I used Selenium to automate the scrapping of the latest 60 reviews posted in the website of more than 1000 titles. The clean version contains a total of 22512 reviews. The main usage is sentiment prediction.",
#                 className="card-text",
#             ),
#             dbc.Row([
#                 dbc.Col(html.A(html.Button("Take a look!", style={'color':'dark', 'hight':'1.5rem'}), href='https://github.com/DavidCarricondo/Custom-database-goodreads-reviews'),),
#                 dbc.Col([
#                     dbc.Button('Technologies', id='popover-target4', style={'color':'primary', 'height':'2rem', 'vertical-align':'top'}),
#                     dbc.Popover([
#                         dbc.PopoverBody(dcc.Markdown(
#                             '''
#                             + Selenium 
#                             + pandas 
#                             + seaborn
#                             + web scraping
#                             '''))
#                     ],id='popover4', is_open=False, target='popover-target4')
#                 ])
#             ])
#         ]
#     ),
# ]


# card_content_5 = [
#     dbc.CardImg(src=app.get_asset_url('pipeline_image.png'), top=True, style={'height':'14rem'}),
#     dbc.CardBody(
#         [
#             html.H4(dcc.Markdown("**Pipeline-project: Dancing to your band**"), className="card-title"),
#             html.P(
#                 "Data pipelines that uses a kaggle data set enriched with data from two different APIS (with and without APIKEY) and from wikipedia scrapping that generate a report on a given music band.",
#                 className="card-text",
#             ),
#             dbc.Row([
#                 dbc.Col(html.A(html.Button("Take a look!", style={'color':'dark', 'hight':'1.5rem'}), href='https://github.com/DavidCarricondo/data-analysis-pipeline'),),
#                 dbc.Col([
#                     dbc.Button('Technologies', id='popover-target5', style={'color':'primary', 'height':'2rem', 'vertical-align':'top'}),
#                     dbc.Popover([
#                         dbc.PopoverBody(dcc.Markdown(
#                             '''
#                             + API request 
#                             + Beautiful soup 
#                             + argparse
#                             + fpdf for pdf generation
#                             + matplotlib
#                             + data pipeline
#                             '''))
#                     ],id='popover5', is_open=False, target='popover-target5')
#                 ])
#             ])
#         ]
#     ),
# ]

# card_content_6 = [
#     dbc.CardImg(src=app.get_asset_url('diamonds_image.png'), top=True, style={'height':'14rem'}),
#     dbc.CardBody(
#         [
#             html.H4(dcc.Markdown("**Diamond prices prediction with ML**"), className="card-title"),
#             html.P(
#                 "Data exploration, cleaning and modelling of a diamonds dataset. I use SciKit-learn and H2O as machine learning frameworks",
#                 className="card-text",
#             ),
#             html.Hr(),
#             dbc.Row([
#                 dbc.Col(html.A(html.Button("Take a look!", style={'color':'dark', 'hight':'1.5rem'}), href='https://github.com/DavidCarricondo/Diamond-prices-ML-Kaggle-competition'),),
#                 dbc.Col([
#                     dbc.Button('Technologies', id='popover-target6', style={'color':'primary', 'height':'2rem', 'vertical-align':'top'}),
#                     dbc.Popover([
#                         dbc.PopoverBody(dcc.Markdown(
#                             '''
#                             + Scikit learn
#                             + Pandas 
#                             + Matplotlib
#                             + Seaborn
#                             + Machine learning
#                             + GridSearshCV
#                             + H2O
#                             '''))
#                     ],id='popover6', is_open=False, target='popover-target6')
#                 ])
#             ])
#         ]
#     ),
# ]

# card_content_7 = [
#     dbc.CardImg(src=app.get_asset_url('mongo_image.png'), top=True, style={'height':'14rem'}),
#     dbc.CardBody(
#         [
#             html.H4(dcc.Markdown("**Choosing best location for company**"), className="card-title"),
#             html.P(
#                 "In this project I make extensive use of mongo queries on unstructure data extracted from different APIs.",
#                 className="card-text",
#             ),
#             html.Hr(),
#             dbc.Row([
#                 dbc.Col(html.A(html.Button("Take a look!", style={'color':'dark', 'hight':'1.5rem'}), href='https://github.com/DavidCarricondo/mongo-project'),),
#                 dbc.Col([
#                     dbc.Button('Technologies', id='popover-target7', style={'color':'primary', 'height':'2rem', 'vertical-align':'top'}),
#                     dbc.Popover([
#                         dbc.PopoverBody(dcc.Markdown(
#                             '''
#                             + MongoDb 
#                             + pymongo 
#                             + API request
#                             + folium
#                             '''))
#                     ],id='popover7', is_open=False, target='popover-target7')
#                 ])
#             ])
#         ]
#     ),
# ]

# card_content_8 = [
#     dbc.CardImg(src=app.get_asset_url('profile_image.png'), top=True, style={'height':'14rem'}),
#     dbc.CardBody(
#         [
#             html.H4(dcc.Markdown("**My profile dashboard**"), className="card-title"),
#             html.P(
#                 "I created a dashboard with dash as a profile of my most relevant data projects.",
#                 className="card-text",
#             ),
#             html.Hr(),
#             html.Hr(),
#             html.Hr(),
#             html.Hr(),
#             dbc.Row([
#                 dbc.Col(html.A(html.Button("Take a look!", style={'color':'dark', 'hight':'1.5rem'}), href='https://github.com/DavidCarricondo/dash-profile'),),
#                 dbc.Col([
#                     dbc.Button('Technologies', id='popover-target8', style={'color':'primary', 'height':'2rem', 'vertical-align':'top'}),
#                     dbc.Popover([
#                         dbc.PopoverBody(dcc.Markdown(
#                             '''
#                             + Dash 
#                             + Dashboards 
#                             + HTML
#                             + Heroku
#                             + App deployment
#                             '''))
#                     ],id='popover8', is_open=False, target='popover-target8')
#                 ])
#             ])
#         ]
#     ),
# ]

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavLink(html.Img(src=app.get_asset_url('linkedin_image.png'), style={'height':'95%', 'width':'25%', 'text-align':'right'}), href='https://www.linkedin.com/in/david-carricondo-sanchez/', className='lead'),
        dbc.NavLink(html.Img(src=app.get_asset_url('github_image.png'),style={'height':'95%', 'width':'25%'}), href='https://github.com/DavidCarricondo', className='lead'),
            
    ],
    brand="You can know more about me here: ",
    brand_href="",
    color="dark",
    dark=True
)

text_card = html.Div([html.H4('Take a look at my data science projects', className='card-header', style={'color': 'primary', 'text-align': 'center'}), 
    html.Div(dcc.Markdown('''
    Thanks for visiting my profile! These are the most relevant data project I have been working on. Click on the **Take a look!**\
         button in each card to be redirected to the *github page* of the project. Click on **Technologies** to pop up the main tools used. \
             If you want to **know more about me**, click on the links in the footer. 
             
                                    Enjoy your stay!
             '''), className='card-text')], className="card border-success mb-3")
