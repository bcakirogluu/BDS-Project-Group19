from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import data
import charts

def get_app_description():
    description_text = '''
        Welcome to ArchiGent
        '''
    return dcc.Markdown(children=description_text)


def get_data_insights():
    insights = '''
        Are you attempting to find out information about historical buildings within Ghent? Look no further. 
        Simply select one of the locations within our map of Ghent and we will provide you with information about your selected building.
        Enjoy!
    '''
    return dcc.Markdown(children=insights)

def get_map_insights():
    map_insights = '''
        The Map at the bottom displays the distribution of all listings over Ghent city by the scatters. 
        The radio items provide the ability to filter the listings by room type. 
        Besides, the Choropleth map represents the average price of each neighbourhood. 
    '''
    return dcc.Markdown(children=map_insights)

def get_source_text():
    source_text = '''
    Data from [Inside Airbnb](http://insideairbnb.com/get-the-data.html),
    licensed under [Creative Commons Attribution 4.0 International
    License](https://creativecommons.org/licenses/by/4.0/).
    '''
    return dcc.Markdown(children=source_text)

def get_map():
    return dbc.Row(
        dbc.Col(
            [
                html.H2("Exercise 3: Map", style={"margin-top": "1em"}),
                get_map_insights(),
                dcc.RadioItems(
                    options=[{"label": "English", "value": "en"}, {"label": "Nederlands", "value": "nl"}, {"label": "Francais", "value": "fr"}, {"label": "Español", "value": "es"}, {"label": "Deutsch", "value": "de"}],
                    value="en",
                    id='ex3-radioitems',
                    labelStyle={'cursor': 'pointer', 'margin-left': '20px'}
                    ),
                dcc.Graph(
                    id="ex3-map",
                    figure=charts.get_map()
                    ),
                html.Div([
                    dcc.Markdown("""
                        **Click Data**

                        Click on points in the graph.
                    """),
                    html.Pre(id='click-data'),
                ], className='three columns')
                
            ],
        )
    )

#https://github.com/plotly/dash/issues/71 for adding the images with a callback, could be useful when we are retrieving images in the future
#https://dash-bootstrap-components.opensource.faculty.ai/docs/components/carousel/ how to add extra features for the images
def get_app_layout():
    return dbc.Container(
        [
            html.H1(children='ArchiGhent',
                    style={"margin-top": "1rem"}),
            get_app_description(),
            get_data_insights(),
            get_map(),
            dbc.Row(
                [
                    #dbc.Col(html.Img(src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPEAAADRCAMAAAAquaQNAAAAFVBMVEUAAADvM0D92iW+pBz/3ib4ri7uI0H4ag0rAAAA6ElEQVR4nO3PMREAIAwEsAIF/5Jr4icucZCqsNM7qe9bWemwsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsfFP4wF6L9AwC9pq5wAAAABJRU5ErkJggg=='), width="auto"),
                    # dbc.Col(html.Section(id="carousel-fade", children=[
                    #             html.Div(id="carousel-fade2", children=[
                    #                 html.Div(id="image"),
                    #                 dcc.Interval(id='interval', interval=3000)
                    #             ])
                    #         ]), width="auto"),
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "http://placeimg.com/625/225/any"},
                            {"key": "2", "src": "http://placeimg.com/625/225/animals"},
                            {"key": "3", "src": "http://placeimg.com/625/225/arch"},
                        ],
                        className="carousel-fade",
                    )
                ],
                justify="between",
                style={"margin-top": "3rem"}),
            dbc.Row(
                [
                    dbc.Col(html.P("Group 19")),
                    dbc.Col(get_source_text(), width="auto")
                ],
                justify="between",
                style={"margin-top": "3rem"})
        ],
        fluid=True,
    )
