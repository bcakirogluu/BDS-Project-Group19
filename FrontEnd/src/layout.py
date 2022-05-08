from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import data
import charts

def get_app_description():
    description_text = '''
        This Dashboard shows how Airbnb impacts neighbourhoods in Flemish Region, Ghent.
        '''
    return dcc.Markdown(children=description_text)


def get_data_insights():
    insights = '''
        In the first chart, the desired neighbourhood is filtered and the number of rooms available from which type is displayed. 
        The distribution of room type over a neighbourhood can be observed by selecting a specific neighbourhood in the dropdown. 
        In the second chart, the room prices in the neighbourhoods are displayed. 
        The third chart presents a histogram of available days in a year, the filtering by "Room type" is provided via radio items.

        As can see from these charts, the majority of the listings is "Entire home/apt".
        The number of rooms which are available more than 200 days per year is high.
        As a result, although the rooms are available, long-term renters such as students still suffer from finding a stay.
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
                    options=data.room_type_options,
                    value='all',
                    id='ex3-radioitems',
                    labelStyle={'cursor': 'pointer', 'margin-left': '20px'}
                    ),
                dcc.Graph(
                    id="ex3-map",
                    figure=charts.get_map()
                    )
                
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
