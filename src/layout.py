import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from src.app_dash import app

def generate_card(project_number, project_dictionary, spaces=0):
    proj = project_dictionary[str(project_number)]
    cardbody = [html.H4(dcc.Markdown(proj['title']), className="card-title"),
                html.P(proj['desc'], className="card-text")]

    for i in range(spaces):
        cardbody.append(html.Hr())

    cardbody.append(dbc.Row([
                    dbc.Col(html.A(html.Button("Take a look!", style={'color':'dark', 'hight':'1.5rem'}), href=proj['link']),),
                    dbc.Col([
                        dbc.Button('Technologies', id='popover-target'+str(project_number), style={'color':'primary', 'height':'2rem', 'vertical-align':'top'}),
                        dbc.Popover([
                            dbc.PopoverBody(dcc.Markdown(proj['technologies']))
                        ],id='popover'+str(project_number), is_open=False, target='popover-target'+str(project_number))
                    ])
                    ])
                )

    card_content = [
        dbc.CardImg(src=app.get_asset_url(proj['image']), top=True, style={'height':'14rem'}),
        dbc.CardBody(cardbody),
    ]

    return card_content


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavLink(html.Img(src=app.get_asset_url('linkedin_image.png'), style={'height':'75%', 'width':'18%', 'text-align':'right'}), href='https://www.linkedin.com/in/david-carricondo-sanchez/', className='lead'),
        dbc.NavLink(html.Img(src=app.get_asset_url('github_image.png'),style={'height':'75%', 'width':'18%'}), href='https://github.com/DavidCarricondo', className='lead'),
        dbc.NavLink(html.Img(src=app.get_asset_url('resume_image.png'),style={'height':'75%', 'width':'18%'}), href='https://drive.google.com/file/d/1sUYw4Xm1cSuaFKVdk-jpG7C1Uz8_SViO/view?usp=sharing', className='lead'),
            
    ],
    brand="A bit more about me: ",
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
