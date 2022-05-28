from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import charts

def get_app_description():
    description_text = '''
        ## Welcome to ArchiGent
        '''
    return dcc.Markdown(children=description_text)


def get_data_insights():
    insights = '''
        Are you attempting to find out information about historical buildings within Ghent? Look no further. 
        Simply select one of the locations within our map of Ghent and we will provide you with information about your selected building.
        Enjoy!
    '''
    return dcc.Markdown(children=insights)

def get_source_text():
    source_text = '''
    Data from [Stad Gent](https://stad.gent/sparql),
    licensed under [Creative Commons Attribution 4.0 International
    License](https://creativecommons.org/licenses/by/4.0/).
    '''
    return dcc.Markdown(children=source_text)

#https://github.com/plotly/dash/issues/71 for adding the images with a callback, could be useful when we are retrieving images in the future
#https://dash-bootstrap-components.opensource.faculty.ai/docs/components/carousel/ how to add extra features for the images
def get_app_layout():
    return dbc.Col([
        dbc.Row([
            get_app_description(),
            get_data_insights()
            ]),
        dbc.Row([
            dbc.Col([
                dcc.RadioItems(
                        options=[{"label": "English", "value": "en"}, {"label": "Nederlands", "value": "nl"}, {"label": "Francais", "value": "fr"}, {"label": "Español", "value": "es"}, {"label": "Deutsch", "value": "de"}],
                        value="en",
                        id='radioitems',
                        labelStyle={'cursor': 'pointer', 'margin-right': '20px'},
                        # style={'margin-left':'0px'}
                    ),
                dcc.Graph(
                        id="map",
                        figure=charts.get_map(),
                        # style={"margin-left":"0px", "padding":"0px"}
                    )
                ], style={'width':'48%'},                
                ),
            dbc.Col([
                    html.Pre(id='click-data')
                ], style={'width':'48%'}
                )
            ], style={},),
        dbc.Row([
                dbc.Col(html.P("Group 19")),
                dbc.Col(get_source_text(), width="auto")
            ])
    ], style={'margin':'30px'}) 
