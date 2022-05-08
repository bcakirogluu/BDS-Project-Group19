# Define functions to return your charts in this file. You could also read in the data here.
import plotly.express as px
from dash import dcc
import data

def get_map(room_type=None):
    if room_type == None or room_type == 'all':
        df = data.listings
    else:
        df = data.listings[data.listings['room_type'] == room_type]
    
    fig1 = px.scatter_mapbox(df,
                             lat='latitude',
                             lon='longitude',
                             #color='room_type',
                             hover_name='name', 
                             hover_data={'latitude':False, 'longitude':False, 'host_name':True, 'price':True, 'room_type':True},
                             labels={
                                 'host_name': 'Host name',
                                 'room_type': 'Room types',
                                 },
                             #color_discrete_sequence=px.colors.sequential.Viridis,
                             # zoom=11,
                             mapbox_style='open-street-map')
    
    neighbourhood_ranks = data.listings.groupby(['neighbourhood']).agg(neighbourhood=('neighbourhood', 'first'), price=('price', 'mean'))
    
    fig2 = px.choropleth_mapbox(neighbourhood_ranks,
                                geojson=data.neighbourhoods_geo,
                                featureidkey="properties.neighbourhood",
                                locations='neighbourhood',
                                color='price',
                                # range_color=[10, 200],
                                color_continuous_scale='reds',
                                hover_name='neighbourhood',
                                hover_data={'neighbourhood':False, 'price':False},
                                zoom=12,
                                center={"lat": 51.0527, "lon": 3.7218},
                                opacity=0.6,
                                mapbox_style='open-street-map')
    
    fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    fig2.add_trace(
        fig1.data[0]
    )
    
    return fig2