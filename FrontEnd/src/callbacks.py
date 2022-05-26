from dash.dependencies import Input, Output, State
from dash import html
import dash_bootstrap_components as dbc
import charts
# import pandas as pd
# import plotly.express as px

def register_callbacks(app):

    @app.callback(
    Output('ex3-map', 'figure'),
    Input('ex3-radioitems', 'value')
    )
    def update_figure(value):
        return charts.get_map(value)

    @app.callback(
    Output('click-data', 'children'),
    Input('ex3-map', 'clickData'))
    def display_click_data(clickData):
        if clickData is not None:
            return clickData['points'][0].get("customdata")[3]
        return ""

    # @app.callback(Output('image', 'children'),
    #           [Input('interval', 'n_intervals')])
    # def display_image(n):
    #     if n == None or n % 3 == 1:
    #         img = html.Img(src="http://placeimg.com/625/225/any")
    #     elif n % 3 == 2:
    #         img = html.Img(src="http://placeimg.com/625/225/animals")
    #     elif n % 3 == 0:
    #         img = html.Img(src="http://placeimg.com/625/225/arch")
    #     else:
    #         img = "None"
    #     return img

#     @app.callback(
#     Output("carousel", "children"), Input("carouselNum", "integer"),
#     )
#     def update_carousel(carouselNum):
#         if n % 2 > 0:
#             carousel1 = dbc.Carousel(
#             items=[{"key": "1", "src": img1}, {"key": "2", "src": img2}],
#             controls=True,
#             indicators=True,
#             style=img_style,
# )

# carousel2 = dbc.Carousel(
#     items=[{"key": "3", "src": img3}, {"key": "4", "src": img4}],
#     controls=True,
#     indicators=True,
#     style=img_style,
# )
#             return carousel2
#         return carousel1

