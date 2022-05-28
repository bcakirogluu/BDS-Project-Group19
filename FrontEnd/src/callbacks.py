from dash.dependencies import Input, Output
from dash import html
import dash_bootstrap_components as dbc
import charts
from data import getImages, getRecords
from dash import dash_table as dt

def register_callbacks(app):

    @app.callback(
    Output('map', 'figure'),
    Input('radioitems', 'value')
    )
    def update_figure(value):
        return charts.get_map(value)

    @app.callback(
    Output('click-data', 'children'),
    Input('map', 'clickData'))
    def display_click_data(clickData):
        if clickData is not None:
            attraction_name = clickData['points'][0].get("customdata")[2]
            attraction_desc = clickData['points'][0].get("customdata")[3]
            attraction_uri = clickData['points'][0].get("customdata")[4]
            images = getImages(attraction_uri)
            if len(images) == 0:
                images = [
                            {"key": "1", "src": "http://placeimg.com/625/225/any"},
                            {"key": "2", "src": "http://placeimg.com/625/225/animals"},
                            {"key": "3", "src": "http://placeimg.com/625/225/arch"},
                        ]
            image_slider = dbc.Carousel(
                        items=images,
                        className="carousel-fade",
                    )
            records_df = getRecords(attraction_uri)
            if records_df.shape[0] == 0:
                text = "There is no record related to this attraction."
                record_dt = ""
            else:
                text = "Records related to this attraction:"
                record_dt = dt.DataTable(id="table-container",
                                         columns=[{'name': 'Museums', 'id': 'museum'},
                                                  {'name': 'Records', 'id': 'title'}],
                                         data=records_df.to_dict("records"),
                                         editable=False,
                                         style_header={'textAlign': 'left'},
                                         style_cell={'textAlign': 'left'},
                                         page_action="native",
                                         page_current= 0,
                                         page_size= 10)                                         
            row = dbc.Row([
                html.H4(children=attraction_name),
                html.H6(children=attraction_desc),
                image_slider,
                html.H6(children=text, style={"margin-top": "20px"}),
                record_dt
                ]
            )
            return row
        return ""